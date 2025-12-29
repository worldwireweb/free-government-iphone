#!/usr/bin/env python3
"""
Script to update tablet button links in free-government-tablet.html to redirect to world-wire.com URLs
"""

import re

# Read the tablet HTML file
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'r') as f:
    content = f.read()

# Tablet URL mappings (blog filename -> world-wire slug)
# Most follow the pattern: blog/[slug].html -> world-wire.com/[slug]/
tablet_slugs = [
    'acp-free-tablet',
    'tablet-with-food-stamps',
    'tablet-with-p-ebt',
    'tablet-with-medicaid',
    'free-tablets-for-seniors',
    'qlink-wireless-tablet',
    't-mobile-free-tablet',
    'standup-wireless-tablet',
    'excess-telecom-tablet',
    'airtalk-wireless-tablet',
    'unity-wireless-tablet',
    'sano-health-tablet',
    'skyway-wireless-tablet',
    'easy-wireless-tablet',
    'culture-wireless-tablet',
    'moolah-wireless-tablet',
    'cintex-wireless-tablet',
    'newphone-wireless-tablet',
    'tablet-with-ssi',
    'tablets-for-low-income',
    'tablets-for-students',
    'tablets-for-disabled',
    'tablet-in-florida',
    'tablet-in-texas',
    'tablet-in-california',
    'tablet-in-georgia',
    'track-your-tablet',
    'acp-tablet-status',
    'free-tablet-food-stamps-florida',
    'gen-mobile-tablet',
    'maxsip-telecom-tablet',
    'windstream-ebb-tablet',
    '5g-government-tablet',
    'vortex-government-tablets',
    'public-wireless-tablet',
    'free-tablets-veterans',
    'm8l-tablet-government',
    'sky-devices-elite-t8',
    'government-tablet-california',
    'government-tablet-florida',
    'safelink-tablet',
    'whoop-connect-tablet',
    'cellution-tablet',
    'vortex-tab-8-4g',
    'tablet-phone-government',
    'reset-maxsip-tablet',
    'tablet-disabled',
    'maxwest-nitro-8',
    'wrazzle-wireless-tablet',
    'metropcs-tablet',
    'grandpad-seniors',
    'wireless-now-tablet',
    '10-dollar-tablet',
    'acp-tablet-near-me',
    'tablet-ebt-georgia',
    'tone-communication-tablet',
    'hoop-wireless-tablet',
    'att-tablet',
    'ebb-tablet',
    'tmobile-tablet-seniors',
    'torch-wireless-tablet',
    'cloud-mobile-tablet',
    'city-communications-tablets',
    'u2-connect-tablet',
    '100-off-tablet-acp',
    'foxxd-t8-tablet',
    'maxwest-astro-8r',
    'x-mobile-tablet',
    'qlink-scepter-8',
    'lte-wireless-tablet',
    'truconnect-tablet',
    'texas-tablet-program',
    'go-md-usa-tablet',
    'verizon-tablet',
    'free-samsung-tablet',
    'go-tech-management-tablet',
    'assurance-wireless-tablet',
    'tmobile-tablet-ebt',
    'tablet-snap-benefits',
    'free-government-tablet',
    'moxee-tablet',
    'sky-devices-government',
    'boost-mobile-tablet',
    'techowl-tablet',
    'cathect-communications',
    'comlink-tablet',
    'nuu-mobile-tablet',
]

# Replace each tablet link
for slug in tablet_slugs:
    old_pattern = f'href="blog/{slug}.html"'
    new_url = f'href="https://world-wire.com/{slug}/?utm_source=iphone_portal&utm_medium=tablet_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal"'
    content = content.replace(old_pattern, new_url)

# Write the updated content back
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'w') as f:
    f.write(content)

print("✓ Updated all tablet links in free-government-tablet.html")
