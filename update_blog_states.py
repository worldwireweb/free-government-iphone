#!/usr/bin/env python3
"""
Script to update state button links in blog.html to redirect to world-wire.com URLs
"""

import re

# Read the blog.html file
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/blog.html', 'r') as f:
    content = f.read()

# State URL mappings from homepage (blog filename -> world-wire slug)
state_mappings = {
    'free-government-phones-maryland': 'free-government-phones-maryland',
    'free-government-phone-tennessee': 'free-government-phone-tennessee',
    'free-government-phone-hawaii': 'free-government-phone-hawaii',
    'free-government-phone-wisconsin': 'free-government-phone-wisconsin',
    'free-government-phone-in-texas': 'free-government-phone-texas',
    'free-government-phone-illinois': 'free-government-phone-illinois',
    'free-government-phone-kentucky': 'free-government-phone-kentucky',
    'free-government-phone-washington-state': 'free-government-phone-washington',
    'free-government-phone-indiana': 'free-government-phone-indiana',
    'free-government-phone-iowa': 'free-government-phone-iowa',
    'free-government-phones-pennsylvania': 'free-government-phones-pennsylvania',
    'free-government-phones-new-jersey': 'free-government-phones-new-jersey',
    'free-government-phone-california': 'free-government-phone-california',
    'free-government-phones-oregon': 'free-government-phones-oregon',
    'free-government-phones-mississippi': 'free-government-phones-mississippi',
    'free-government-phone-ohio': 'free-government-phone-ohio',
    'free-government-phone-louisiana': 'free-government-phone-louisiana',
    'free-government-phones-new-york': 'free-government-phones-new-york',
    'free-government-phone-florida': 'free-government-phone-florida',
    'free-government-phone-georgia': 'free-government-phone-georgia',
    'free-government-phone-alabama': 'free-government-phone-alabama',
    'free-government-phone-michigan': 'free-government-phone-michigan',
    'free-government-phones-kansas': 'free-government-phones-kansas',
    'free-government-phones-west-virginia': 'free-government-iphone-11',  # From homepage
    'free-government-phones-arkansas': 'free-government-phones-arkansas',
    'free-government-phones-nc': 'free-government-iphone-7',  # From homepage
    'free-government-phone-arizona': 'free-government-phone-arizona',
    'free-government-phones-colorado': 'free-government-phones-colorado',
    'free-government-phones-alaska': 'free-government-tablet-florida',  # From homepage
    'free-government-phones-connecticut': 'free-government-phones-connecticut',
    'free-government-phones-delaware': 'free-government-phones-delaware',
    'free-government-phones-idaho': 'free-government-iphone-8-plus',  # From homepage
    'free-government-phones-maine': 'free-government-iphone-7-plus',  # From homepage
    'free-government-phones-massachusetts': 'ebb-program-free-laptop',  # From homepage
    'free-government-phones-minnesota': 'free-government-iphone-5',  # From homepage
    'free-government-phones-missouri': 'free-iphone-6s-government-phone',  # From homepage
    'free-government-phones-montana': 'free-government-iphone-6-plus',  # From homepage
    'free-government-phones-nebraska': 'free-government-iphone-12-mini',  # From homepage
    'free-government-phones-nevada': 'free-government-iphone-15',  # From homepage
    'free-government-phones-new-hampshire': 'free-laptop-for-college-student',  # From homepage
    'free-government-phones-new-mexico': 'free-government-iphone-8',  # From homepage
    'free-government-phones-north-dakota': 'free-government-iphone-x',  # From homepage
    'free-government-phones-oklahoma': 'free-government-iphone-xr',  # From homepage
    'free-government-phones-rhode-island': 'free-iphone-with-ebb-program',  # From homepage
    'free-government-phones-south-carolina': 'free-government-phones-south-carolina',
    'free-government-phones-south-dakota': 'free-government-iphone-13-pro-max',  # From homepage
    'free-government-phones-utah': 'free-iphone-15-pro-max',  # From homepage
    'free-government-phones-vermont': 'free-iphone-16-government-phone-for-everyone',  # From homepage
    'free-government-phones-virginia': 'free-government-iphone-14',  # From homepage
    'free-government-phones-wyoming': 'free-iphone-13-government-phone',  # From homepage
}

# Replace each state link
for blog_slug, world_wire_slug in state_mappings.items():
    old_pattern = f'href="blog/{blog_slug}.html"'
    new_url = f'href="https://world-wire.com/{world_wire_slug}/?utm_source=iphone_portal&utm_medium=blog_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal"'
    content = content.replace(old_pattern, new_url)

# Write the updated content back
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/blog.html', 'w') as f:
    f.write(content)

print("✓ Updated all state links in blog.html")
