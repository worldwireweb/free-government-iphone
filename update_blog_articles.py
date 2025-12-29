#!/usr/bin/env python3
"""
Script to update sidebar links in all blog article HTML files to redirect to world-wire.com URLs
"""

import os
import glob
import re

blog_dir = '/Users/macos/free-government-iPhone-11/free-government-iphone/blog'

# Common sidebar link mappings (local blog -> world-wire)
sidebar_mappings = {
    # Popular iPhone Offers
    'free-government-iphone-13.html': 'https://world-wire.com/free-iphone-13-government-phone/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-government-iphone-14.html': 'https://world-wire.com/free-government-iphone-14/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-government-iphone-15.html': 'https://world-wire.com/free-government-iphone-15/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-iphone-16-government-phone-for-everyone.html': 'https://world-wire.com/free-iphone-16-government-phone-for-everyone/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    
    # States
    'free-government-phone-california.html': 'https://world-wire.com/free-government-phone-california/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-government-phone-in-texas.html': 'https://world-wire.com/free-government-phone-texas/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-government-phone-florida.html': 'https://world-wire.com/free-government-phone-florida/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    'free-government-phones-new-york.html': 'https://world-wire.com/free-government-phones-new-york/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    
    # Navigation links
    '../samsung-phones.html': 'https://world-wire.com/free-samsung-government-phone/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    '../laptops.html': 'https://world-wire.com/free-government-laptop/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    '../tablets.html': 'https://world-wire.com/free-government-tablet-in-california/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
    '../free-5g-phones.html': 'https://world-wire.com/free-5g-government-phones/?utm_source=iphone_portal&utm_medium=blog_article&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal',
}

# Get all HTML files in blog directory
html_files = glob.glob(os.path.join(blog_dir, '*.html'))

updated_count = 0

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace each sidebar link
        for old_href, new_url in sidebar_mappings.items():
            # Match href="..." pattern
            old_pattern = f'href="{old_href}"'
            new_pattern = f'href="{new_url}"'
            content = content.replace(old_pattern, new_pattern)
        
        # Only write if content changed
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
    
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

print(f"✓ Updated sidebar links in {updated_count} blog article files")
