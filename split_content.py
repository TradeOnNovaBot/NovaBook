#!/usr/bin/env python3

import re
import os
import sys

def slugify(text):
    """Convert text to slug format."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

def split_markdown(input_file, output_dir):
    """Split a markdown file into separate files based on sections."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip the table of contents
    if '# Table of Contents' in content:
        parts = content.split('---\n\n', 1)
        if len(parts) > 1:
            content = parts[1]
    
    # Split by markdown horizontal rule
    sections = content.split('\n---\n\n')
    
    for section in sections:
        # Extract the title from the section
        title_match = re.search(r'# (.*?)(\n|$)', section)
        if title_match:
            title = title_match.group(1)
            filename = slugify(title) + '.md'
            
            # Write the section to a file
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(section)
            
            print(f"Created {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split_content.py <input_markdown_file> <output_directory>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    split_markdown(input_file, output_dir) 