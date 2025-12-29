#!/usr/bin/env python3
"""
Script to revert blog.html buttons to link to local blog articles instead of world-wire.com
"""

# Read the blog HTML file
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/blog.html', 'r') as f:
    content = f.read()

# iPhone model mappings (world-wire slug -> local blog file)
iphone_mappings = {
    'free-government-iphone-5': 'blog/free-government-iphone-5.html',
    'free-government-iphone-6-plus': 'blog/free-government-iphone-6-plus.html',
    'free-iphone-6s-government-phone': 'blog/free-government-iphone-6s.html',
    'free-government-iphone-7': 'blog/free-government-iphone-7.html',
    'free-government-iphone-7-plus': 'blog/free-government-iphone-7-plus.html',
    'free-government-iphone-8': 'blog/free-government-iphone-8.html',
    'free-government-iphone-8-plus': 'blog/free-government-iphone-8-plus.html',
    'free-government-iphone-se': 'blog/free-government-iphone-se.html',
    'free-government-iphone-x': 'blog/free-government-iphone-x.html',
    'free-government-iphone-xr': 'blog/free-government-iphone-xr.html',
    'free-government-iphone-11': 'blog/free-government-iphone-11.html',
    'free-government-iphone-12': 'blog/free-government-iphone-12.html',
    'free-government-iphone-12-mini': 'blog/free-government-iphone-12-mini.html',
    'free-government-iphone-12-pro-max': 'blog/free-government-iphone-12-pro-max.html',
    'free-iphone-13-government-phone': 'blog/free-government-iphone-13.html',
    'free-government-iphone-13-mini': 'blog/free-government-iphone-13-mini.html',
    'free-government-iphone-13-pro-max': 'blog/free-government-iphone-13-pro-max.html',
    'free-government-iphone-14': 'blog/free-government-iphone-14.html',
    'free-government-iphone-14-pro-max': 'blog/free-government-iphone-14-pro-max.html',
    'free-government-iphone-15': 'blog/free-government-iphone-15.html',
    'free-iphone-15-pro-max': 'blog/free-government-iphone-15-pro-max.html',
    'free-iphone-16-government-phone-for-everyone': 'blog/free-iphone-16-government-phone-for-everyone.html',
}

# Carrier/Program mappings
carrier_mappings = {
    'free-iphone-with-food-stamps': 'blog/iphone-with-food-stamps.html',
    'newphone-wireless-free-iphone': 'blog/newphone-wireless.html',
    'cricket-free-iphone': 'blog/cricket-wireless.html',
    'safelink-free-iphone': 'blog/safelink-wireless.html',
    'free-iphone-from-verizon': 'blog/verizon-free-iphone.html',
    'free-iphone-with-ebb-program': 'blog/ebb-program-iphone.html',
    'free-iphone-7-with-food-stamps': 'blog/iphone-7-food-stamps.html',
    'boost-mobile-free-iphone-11': 'blog/boost-mobile-iphone-11.html',
    'xfinity-mobile-free-iphone': 'blog/xfinity-mobile.html',
    'airtalk-wireless-free-iphone': 'blog/airtalk-wireless-iphone.html',
    'cintex-wireless-free-iphone': 'blog/cintex-wireless-iphone.html',
}

# State mappings (using the ones from homepage)
state_mappings = {
    'free-government-phones-maryland': 'blog/free-government-phones-maryland.html',
    'free-government-phone-tennessee': 'blog/free-government-phone-tennessee.html',
    # Add more as needed...
}

# Replace world-wire.com URLs with local blog URLs
import re

all_mappings = {**iphone_mappings, **carrier_mappings, **state_mappings}

for ww_slug, local_path in all_mappings.items():
    # Pattern to match world-wire.com URL with UTM parameters
    pattern = f'https://world-wire.com/{ww_slug}/\\?utm_source=iphone_portal&utm_medium=blog_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal'
    content = content.replace(pattern, local_path)

# Write the updated content back
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/blog.html', 'w') as f:
    f.write(content)

print("✓ Updated blog.html buttons to link to local blog articles")
