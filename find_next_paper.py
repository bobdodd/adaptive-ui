#!/usr/bin/env python3
"""
Find next clean papers to review.
"""

import os

def read_clean_papers():
    """Read clean papers list."""
    with open('clean_papers.txt', 'r', encoding='utf-8') as f:
        # Skip comment lines
        papers = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return papers

def read_reviewed_papers():
    """Read already reviewed papers from COMPREHENSIVE_BIBLIOGRAPHY.md."""
    reviewed = set()
    try:
        with open('COMPREHENSIVE_BIBLIOGRAPHY.md', 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for "File:" lines
            import re
            file_pattern = r'\*\*File:\*\* `referenced papers/[^/]+/([^\.]+)\.pdf`'
            matches = re.findall(file_pattern, content)
            reviewed.update(matches)
    except Exception as e:
        print(f"Error reading reviewed papers: {e}")
    return reviewed

def main():
    clean_papers = read_clean_papers()
    reviewed_papers = read_reviewed_papers()

    print(f"Total clean papers: {len(clean_papers)}")
    print(f"Already reviewed: {len(reviewed_papers)}")

    # Find papers not yet reviewed
    to_review = [p for p in clean_papers if p not in reviewed_papers]
    print(f"Papers to review: {len(to_review)}")

    # Show next 20 papers
    print(f"\nNext 20 papers to review (alphabetical order):")
    for i, paper in enumerate(to_review[:20]):
        print(f"{i+1:3}. {paper}")

    # Also show by rough category grouping
    print(f"\nFirst few papers by rough grouping:")
    groups = {}
    for paper in to_review[:30]:
        # Simple grouping by prefix
        if paper.startswith('p'):
            # Try to extract number
            import re
            match = re.match(r'p(\d+)', paper)
            if match:
                num = int(match.group(1))
                if num < 100:
                    group = 'p00-p99'
                elif num < 200:
                    group = 'p100-p199'
                elif num < 300:
                    group = 'p200-p299'
                else:
                    group = 'p300+'
            else:
                group = 'p-other'
        elif paper.startswith('a'):
            group = 'a-prefix'
        else:
            group = 'other'

        if group not in groups:
            groups[group] = []
        groups[group].append(paper)

    for group in sorted(groups.keys()):
        papers = groups[group]
        print(f"\n{group} ({len(papers)}):")
        for paper in papers[:5]:
            print(f"  - {paper}")
        if len(papers) > 5:
            print(f"  ... and {len(papers) - 5} more")

if __name__ == '__main__':
    main()