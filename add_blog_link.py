#!/usr/bin/env python3
"""
Script to add Blog link to navigation menus on all pages
"""

import re

pages_to_update = [
    'free-government-tablet.html',
    'free-government-laptop.html',
    'free-government-5g-phone.html',
    'free-government-iphone.html',
]

for page in pages_to_update:
    with open(f'/Users/macos/free-government-iPhone-11/free-government-iphone/{page}', 'r') as f:
        content = f.read()
    
    # Pattern to find the 5G Phone link and add Blog after it
    pattern = r'(<a href="free-government-5g-phone.html">5G Phone</a>)'
    replacement = r'\1\n                <a href="blog.html">Blog</a>'
    
    content = re.sub(pattern, replacement, content)
    
    with open(f'/Users/macos/free-government-iPhone-11/free-government-iphone/{page}', 'w') as f:
        f.write(content)
    
    print(f"✓ Added Blog link to {page}")

print("\n✓ All pages updated with Blog link in navigation")
