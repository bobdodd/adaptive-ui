#!/usr/bin/env python3
"""
Analyze which categories have garbled papers.
"""

import csv
import os

def read_garbled_list(filename):
    """Read list of garbled papers from file."""
    with open(filename, 'r', encoding='utf-8') as f:
        # Skip comment lines
        papers = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return papers

def analyze_categories():
    garbled_papers = read_garbled_list('garbled_papers.txt')

    # Read CSV
    categories = {}
    with open('paper_inventory.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row['filename']
            stem = os.path.splitext(os.path.basename(filename))[0]
            category = row['category']

            if stem in garbled_papers:
                if category not in categories:
                    categories[category] = []
                categories[category].append(stem)

    # Print results
    print("Garbled papers by category:")
    for category, papers in sorted(categories.items()):
        print(f"\n{category}: {len(papers)} papers")
        for paper in sorted(papers)[:10]:  # Show first 10
            print(f"  - {paper}")
        if len(papers) > 10:
            print(f"  ... and {len(papers) - 10} more")

if __name__ == '__main__':
    analyze_categories()