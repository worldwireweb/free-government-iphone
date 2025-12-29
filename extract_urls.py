#!/usr/bin/env python3
"""
Extract world-wire.com URLs from blog articles to create homepage button mappings.
"""

import re
from pathlib import Path
import json

def extract_url_from_article(html_file):
    """Extract the main world-wire.com URL from a blog article."""
    content = html_file.read_text()
    
    # Pattern to find world-wire.com URLs in clickbait boxes
    pattern = r'href="(https?://world-wire\.com/[^"]+)"[^>]*class="clickbait-link"'
    matches = re.findall(pattern, content)
    
    if matches:
        # Get the first clickbait link (main CTA)
        url = matches[0]
        # Remove UTM parameters
        clean_url = url.split('?')[0]
        return clean_url
    return None

def main():
    blog_dir = Path('blog')
    url_mapping = {}
    
    # Extract URLs from all blog articles
    for html_file in sorted(blog_dir.glob('*.html')):
        url = extract_url_from_article(html_file)
        if url:
            # Store mapping: filename (without .html) -> URL
            url_mapping[html_file.stem] = url
    
    # Save mapping to JSON file
    output_file = Path('url_mapping.json')
    with output_file.open('w') as f:
        json.dump(url_mapping, f, indent=2, sort_keys=True)
    
    print(f"✓ Extracted {len(url_mapping)} URL mappings")
    print(f"✓ Saved to {output_file}")
    
    # Print some examples
    print("\nExample mappings:")
    for i, (filename, url) in enumerate(sorted(url_mapping.items())[:5]):
        print(f"  {filename} -> {url}")

if __name__ == '__main__':
    main()
