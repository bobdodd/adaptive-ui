#!/usr/bin/env python3
"""
Extract information from referenced papers for bibliography creation.
Processes PDF files and extracts title, authors, abstract, and first page content.
"""

import os
import subprocess
import re
import csv
from collections import Counter
from pathlib import Path

def clean_text(text, max_length=None):
    """Clean text for CSV: remove newlines, extra spaces, limit length."""
    if not text:
        return ''
    # Replace newlines and carriage returns with space
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    if max_length and len(text) > max_length:
        text = text[:max_length] + '...'
    return text

def extract_pdf_metadata(pdf_path):
    """Extract title and author from PDF metadata using pdfinfo."""
    try:
        result = subprocess.run(
            ['pdfinfo', '-raw', pdf_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            metadata = result.stdout
            title = ''
            author = ''
            for line in metadata.split('\n'):
                if line.startswith('Title:'):
                    title = line[6:].strip()
                elif line.startswith('Author:'):
                    author = line[7:].strip()
            return title, author
    except Exception as e:
        pass  # pdfinfo not available or failed
    return '', ''

def fix_garbled_text(text):
    """Attempt to fix garbled character substitutions using known pattern fixes."""
    if not text:
        return text

    # Count suspicious characters
    suspicious = set('#%+3615?m248@>;=')
    total_chars = len(text)
    if total_chars == 0:
        return text
    suspicious_count = sum(1 for c in text if c in suspicious)
    # If less than 2% suspicious, likely not garbled
    if suspicious_count / total_chars < 0.02:
        return text

    # Known pattern fixes derived from observed patterns in garbled PDFs
    pattern_fixes = [
        ('#e', 'The'),   # "#e" -> "The" (common at start of sentences)
        ('t#e', 'the'),  # "t#e" -> "the"
        ('%o', 'wo'),    # "%o" -> "wo"
        ('%orld', 'world'),
        ('pop+lation', 'population'),
        ('a1in1', 'aging'),
        ('n+m3er', 'number'),
        ('%#o', 'who'),
        ('e5perien6in1', 'experiencing'),
        ('f+n6tional', 'functional'),
        ('6apa3ility', 'capability'),
        ('in6rease8', 'increase.'),
        ('desi1n', 'design'),
        ('9in6l+sive', 'inclusive'),
        ('prod+6ts', 'products'),
        ('a66ommodate', 'accommodate'),
        ('%ider', 'wider'),
        ('metri6s', 'metrics'),
        ('s+66ess', 'success'),
        ('s+6#', 'such'),
        ('S+66essf+l', 'Successful'),
        ('in6l+sive', 'inclusive'),
        ('re=+ires', 'requires'),
        ('3alan6e', 'balance'),
        ('3et%een', 'between'),
        ('+sers', 'users'),
        ('alon1', 'along'),
        ('%it#', 'with'),
        ('eval+ation8', 'evaluation.'),
        ('@f', 'If'),
        ('6orre6t', 'correct'),
        ('e56l+sion8', 'exclusion.'),
        ('lsk12Jeng.cam.ac.uk', 'lsk12@eng.cam.ac.uk'),
        ('pjc10Jeng.cam.ac.uk', 'pjc10@eng.cam.ac.uk'),
        ('ma>es', 'makes'),
        ('Honse=+ently', 'Consequently'),
    ]

    # Apply pattern fixes (case-sensitive)
    result = text
    for old, new in pattern_fixes:
        if old in result:
            result = result.replace(old, new)

    # Fix common spacing issues
    spacing_fixes = [
        ('t he ', 'the '),
        ('T he ', 'The '),
        ('w orld', 'world'),
        ('p opulation', 'population'),
    ]
    for old, new in spacing_fixes:
        result = result.replace(old, new)

    return result

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext with multiple strategies."""
    strategies = [
        ['pdftotext', '-layout', '-enc', 'UTF-8', pdf_path, '-'],
        ['pdftotext', '-raw', '-enc', 'UTF-8', pdf_path, '-'],
        ['pdftotext', '-layout', pdf_path, '-'],  # original default
        ['pdftotext', '-raw', pdf_path, '-'],
        ['pdftotext', '-table', '-enc', 'UTF-8', pdf_path, '-'],
        ['pdftotext', '-layout', '-eol', 'unix', '-enc', 'Latin1', pdf_path, '-'],
    ]

    best_text = ""
    best_score = -1

    for cmd in strategies:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0 and result.stdout:
                text = result.stdout
                # Score text by readability: ratio of alphabetic + space + punctuation
                total_chars = len(text)
                if total_chars == 0:
                    continue
                readable_chars = sum(1 for c in text if c.isalpha() or c.isspace() or c in '.,;:!?\'"()-')
                score = readable_chars / total_chars
                # Prefer longer text
                if score > 0.7 and len(text) > 1000:
                    # High quality text
                    best_text = text
                    best_score = score
                    break
                elif score > best_score:
                    best_text = text
                    best_score = score
        except Exception as e:
            continue  # Try next strategy

    # If we have text, try to fix garbled characters
    if best_text:
        best_text = fix_garbled_text(best_text)

    return best_text

def extract_potential_title(text, max_lines=20):
    """Extract potential title from first few lines."""
    lines = text.split('\n')[:max_lines]

    # Look for lines with title-like patterns (not too short, not too long,
    # mixed case, not all caps, not containing common non-title words)
    potential_titles = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        # Skip lines that are obviously not titles
        if len(line) < 10 or len(line) > 200:
            continue
        if line.lower().startswith('abstract') or line.lower().startswith('introduction'):
            break
        if line.lower().startswith('proceedings') or line.lower().startswith('copyright'):
            continue
        # Check for author-like patterns (comma, "and", etc.)
        if re.search(r',.*(university|institute|lab|@)', line, re.IGNORECASE):
            continue
        if re.search(r'\b(and|et al\.?|,)\b', line, re.IGNORECASE):
            continue
        potential_titles.append(line)

    # Return the first non-empty line that seems like a title
    for title in potential_titles:
        if title:
            return title
    return ""

def extract_title_from_text(text):
    """Extract title from PDF text using heuristic."""
    lines = text.split('\n')
    # Skip empty lines at start
    content_lines = []
    for line in lines:
        line = line.strip()
        if line:
            content_lines.append(line)
        if len(content_lines) > 30:
            break

    # Common header patterns to skip
    skip_patterns = [
        r'^proceedings$', r'^conference$', r'^volume$', r'^issue$', r'^issn$',
        r'^chi \d{4}', r'^acm', r'^ieee', r'^copyright', r'^.*proceedings.*$',
        r'^.*symposium.*$', r'^.*workshop.*$', r'^.*conference.*$'
    ]

    # Look for abstract/introduction as stop signal
    stop_words = ['abstract', 'introduction', 'keywords', 'ccs', '1.', '1 ']

    candidates = []
    for line in content_lines:
        line_lower = line.lower()
        # Stop if we hit abstract/introduction
        if any(line_lower.startswith(sw) for sw in stop_words):
            break
        # Skip if matches skip patterns
        if any(re.search(pattern, line_lower) for pattern in skip_patterns):
            continue
        # Skip if line is too long (>200) or too short (<5)
        if len(line) > 200 or len(line) < 5:
            continue
        # Skip if line is all uppercase (might be header)
        if line.isupper():
            continue
        # Skip if contains email or URL
        if '@' in line or 'http' in line:
            continue
        # Skip if contains affiliation keywords
        if re.search(r'university|institute|lab|department|center|school', line_lower):
            continue
        candidates.append(line)

    # If we have candidates, return the first one (likely title)
    if candidates:
        return candidates[0]
    return ""

def extract_authors_from_text(text):
    """Extract authors from PDF text."""
    lines = text.split('\n')
    # Find title line index
    title = extract_title_from_text(text)
    title_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == title:
            title_idx = i
            break
    # If title not found, start from line 0
    start_idx = title_idx + 1 if title_idx >= 0 else 0
    # Examine next 15 lines
    candidate_lines = lines[start_idx:start_idx + 15]
    authors = []
    for line in candidate_lines:
        line = line.strip()
        if not line:
            continue
        # Skip lines that are too long (>150) or too short (<2)
        if len(line) > 150 or len(line) < 2:
            continue
        # Skip lines that are obviously not names (contain numbers, special chars)
        if re.search(r'\d', line):
            continue
        # Skip lines with URL/email (but may contain email after name)
        if '@' in line:
            # Extract name part before '@'
            name_part = line.split('@')[0].strip()
            if name_part and len(name_part) > 3:
                authors.append(name_part)
            continue
        # Skip lines with affiliation keywords (university, institute, lab, department)
        if re.search(r'university|institute|lab|department|center|school', line.lower()):
            continue
        # Look for patterns with commas, 'and', '&' as separators
        if re.search(r'\b(and|&|,)\b', line, re.IGNORECASE):
            authors.append(line)
            continue
        # If line contains common name patterns (capitalized words)
        words = line.split()
        if len(words) >= 1 and len(words) <= 4:
            # Check if each word starts with capital letter
            if all(w[0].isupper() for w in words if w):
                authors.append(line)
    # Deduplicate and join
    if authors:
        # Take first 3 unique authors
        seen = set()
        unique = []
        for a in authors:
            if a not in seen:
                seen.add(a)
                unique.append(a)
        return '; '.join(unique[:3])
    return ""

def extract_potential_authors(text, max_lines=30):
    """Extract potential authors from text after title."""
    lines = text.split('\n')[:max_lines]
    authors = []

    # Look for lines after title that contain author names
    # Common patterns: names with affiliations, emails, "by" etc.
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        # Skip if looks like title (already captured)
        if len(line) > 200:
            continue
        # Look for email addresses or affiliations
        if '@' in line or 'university' in line.lower() or 'institute' in line.lower():
            # Extract name part (before email/affiliation)
            name_part = re.split(r'[\[\(@]', line)[0].strip()
            if name_part and len(name_part) > 3:
                authors.append(name_part)
        # Look for "and" or commas separating names
        elif re.search(r'\b(and|&|,)\b', line, re.IGNORECASE):
            authors.append(line)

    return "; ".join(authors[:3]) if authors else ""

def extract_abstract(text):
    """Extract abstract section if present."""
    lines = text.split('\n')
    in_abstract = False
    abstract_lines = []

    for line in lines:
        line_lower = line.lower().strip()
        # Start of abstract
        if line_lower in ['abstract', 'summary', 'synopsis']:
            in_abstract = True
            continue
        # Stop conditions
        if in_abstract and line_lower in ['introduction', 'keywords', 'ccs', 'acm classification', 'author keywords', '1.', '1 introduction', '1. introduction']:
            break
        if in_abstract and line.strip():
            abstract_lines.append(line.strip())
        # Limit to prevent capturing too much
        if len(abstract_lines) > 30:
            break

    # Join with spaces, preserving paragraph breaks as single space
    abstract_text = ' '.join(abstract_lines)
    # Clean extra whitespace
    abstract_text = re.sub(r'\s+', ' ', abstract_text)
    return abstract_text.strip()

def process_papers(root_dir, output_csv, reviews_dir):
    """Process all PDFs in root_dir and write to CSV."""
    Path(reviews_dir).mkdir(exist_ok=True)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'category', 'title', 'authors', 'abstract_preview', 'text_file']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        pdf_count = 0
        for root, dirs, files in os.walk(root_dir):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.lower().endswith('.pdf') and not file.startswith('.'):
                    pdf_path = os.path.join(root, file)
                    relative_path = os.path.relpath(pdf_path, root_dir)

                    # Determine category from directory structure
                    category = os.path.relpath(root, root_dir)
                    if category == '.':
                        category = 'root'

                    print(f"Processing: {relative_path}")

                    # Extract text
                    text = extract_text_from_pdf(pdf_path)

                    if text:
                        # Save extracted text for manual review
                        review_filename = f"{Path(file).stem}_review.txt"
                        review_path = os.path.join(reviews_dir, review_filename)
                        with open(review_path, 'w', encoding='utf-8') as f:
                            f.write(text[:200000])  # First 200k chars (most papers)

                        # Extract information
                        meta_title, meta_author = extract_pdf_metadata(pdf_path)
                        title = meta_title if meta_title else extract_title_from_text(text)
                        if not title:
                            title = extract_potential_title(text)
                        authors = meta_author if meta_author else extract_authors_from_text(text)
                        if not authors:
                            authors = extract_potential_authors(text)
                        abstract = extract_abstract(text)

                        # Clean fields for CSV
                        title_clean = clean_text(title, max_length=300)
                        authors_clean = clean_text(authors, max_length=300)
                        abstract_clean = clean_text(abstract, max_length=300)[:200] if abstract else ''

                        writer.writerow({
                            'filename': relative_path,
                            'category': category,
                            'title': title_clean,
                            'authors': authors_clean,
                            'abstract_preview': abstract_clean,
                            'text_file': review_filename
                        })

                    pdf_count += 1
                    if pdf_count % 10 == 0:
                        print(f"Processed {pdf_count} PDFs...")

        print(f"Total PDFs processed: {pdf_count}")

if __name__ == '__main__':
    root_dir = 'referenced papers'
    output_csv = 'paper_inventory.csv'
    reviews_dir = 'paper_reviews'

    if os.path.exists(root_dir):
        process_papers(root_dir, output_csv, reviews_dir)
        print(f"Output written to {output_csv}")
        print(f"Extracted text files in {reviews_dir}")
    else:
        print(f"Directory '{root_dir}' not found.")