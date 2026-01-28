#!/usr/bin/env python3
"""
Generate markdown bibliography from paper_inventory.csv.
Creates structured entries with placeholders for detailed reviews.
"""

import csv
import os
from collections import defaultdict

def read_csv(csv_path):
    """Read CSV and group by category."""
    papers_by_category = defaultdict(list)

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['category']
            papers_by_category[category].append(row)

    return papers_by_category

def format_citation(row):
    """Format a basic citation from row data."""
    title = row['title'].strip() if row['title'].strip() else 'Unknown Title'
    authors = row['authors'].strip() if row['authors'].strip() else 'Unknown Authors'

    # Simple citation format (can be improved later)
    return f"{authors}. ({row.get('year', 'Unknown Year')}). {title}."

def generate_markdown(papers_by_category, output_path):
    """Generate markdown file with categorized entries."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Comprehensive Bibliography - Auto-generated\n\n")
        f.write("This file contains automatically extracted references from the `referenced papers/` directory.\n")
        f.write("Entries are grouped by category. Detailed reviews will be added manually.\n\n")

        # Sort categories for consistent output
        categories = sorted(papers_by_category.keys())

        for category in categories:
            if category == 'root':
                display_category = 'Root Directory'
            else:
                display_category = category.replace('_', ' ').title()

            f.write(f"## {display_category}\n\n")

            papers = papers_by_category[category]
            # Sort by filename
            papers.sort(key=lambda x: x['filename'])

            for i, paper in enumerate(papers, 1):
                citation = format_citation(paper)
                f.write(f"### {citation}\n\n")
                f.write(f"**File:** `{paper['filename']}`  \n")
                f.write(f"**Category:** {category}  \n")

                if paper['abstract_preview']:
                    f.write(f"**Abstract Preview:** {paper['abstract_preview']}  \n")

                f.write("\n**Summary:** *[Summary to be added]*  \n")
                f.write("\n**Thesis Relevance:** *[Relevance to be added]*  \n")
                f.write("\n**Cross-references:** *[Thesis chapters, models, publications]*  \n")

                f.write("\n---\n\n")

        f.write("\n## Notes\n")
        f.write(f"Total papers: {sum(len(papers) for papers in papers_by_category.values())}\n")
        f.write("Generated from `paper_inventory.csv`. Manual review needed for accuracy.\n")

def main():
    csv_path = 'paper_inventory.csv'
    output_path = 'BIBLIOGRAPHY_AUTO_GENERATED.md'

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found. Run extract_paper_info.py first.")
        return

    papers_by_category = read_csv(csv_path)
    generate_markdown(papers_by_category, output_path)

    print(f"Generated {output_path}")
    print(f"Categories: {len(papers_by_category)}")
    for category, papers in papers_by_category.items():
        print(f"  {category}: {len(papers)} papers")

if __name__ == '__main__':
    main()