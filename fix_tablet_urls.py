#!/usr/bin/env python3
"""
Script to update tablet button links with the correct world-wire.com URLs provided by user
"""

import re

# Read the tablet HTML file
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'r') as f:
    content = f.read()

# Correct URL mappings (old slug -> new correct URL)
url_corrections = {
    'free-tablet-food-stamps-florida': 'free-tablet-with-food-stamps-florida',
    'gen-mobile-tablet': 'gen-mobile-free-tablet',
    'maxsip-telecom-tablet': 'maxsip-telecom-free-tablet',
    'windstream-ebb-tablet': 'windstream-ebb-tablet-free',
    'unity-wireless-tablet': 'unity-wireless-free-tablet',
    '5g-government-tablet': 'free-5g-government-tablet',
    'vortex-government-tablets': 'vortex-government-phones-and-tablets',
    'public-wireless-tablet': 'public-wireless-free-tablet-program',
    'tablet-with-food-stamps': 'get-free-tablets-with-food-stamps-ebt-card',
    'qlink-wireless-tablet': 'q-link-wireless-free-tablet',
    'free-tablets-veterans': 'free-tablets-for-veterans',
    'excess-telecom-tablet': 'excess-telecom-free-tablet',
    'm8l-tablet-government': 'm8l-tablet-free-government',
    'sky-devices-elite-t8': 'sky-devices-elite-t8-tablet',
    'government-tablet-california': 'free-government-tablet-in-california',
    'government-tablet-florida': 'free-government-tablet-florida',
    'safelink-tablet': 'safelink-free-tablet',
    'whoop-connect-tablet': 'whoop-connect-free-tablet',
    'cellution-tablet': 'cellution-free-tablet',
    'vortex-tab-8-4g': 'vortex-tab-8-4g-tablet-for-free',
    'tablet-phone-government': 'free-tablet-with-phone-from-government',
    'reset-maxsip-tablet': 'reset-maxsip-telecom-tablet',
    'tablet-disabled': 'free-tablet-for-disabled',
    'maxwest-nitro-8': 'free-maxwest-nitro-8-tablet',
    'wrazzle-wireless-tablet': 'wrazzle-wireless-free-tablet',
    'metropcs-tablet': 'metropcs-free-tablet',
    'grandpad-seniors': 'grandpad-tablet-for-seniors',
    'wireless-now-tablet': 'wireless-now-free-tablet',
    '10-dollar-tablet': '10-dollar-tablet-from-government',
    'acp-tablet-near-me': 'acp-free-tablet-near-me',
    'tablet-ebt-georgia': 'free-tablet-with-ebt-georgia',
    'tone-communication-tablet': 'tone-communication-free-tablet',
    'tablet-with-p-ebt': 'free-tablet-with-ebt-card',
    'hoop-wireless-tablet': 'hoop-wireless-free-tablet',
    'att-tablet': 'att-free-tablet',
    'ebb-tablet': 'emergency-broadband-benefit-free-tablet',
    'tmobile-tablet-seniors': 't-mobile-free-tablet-for-seniors',
    'airtalk-wireless-tablet': 'airtalk-wireless-free-tablet',
    'torch-wireless-tablet': 'torch-wireless-free-tablet',
    'cloud-mobile-tablet': 'cloud-mobile-tablet-free',
    'city-communications-tablets': 'city-communications-free-tablets',
    'u2-connect-tablet': 'u2-connect-free-tablet',
    '100-off-tablet-acp': 'how-do-i-get-100-off-a-tablet-with-acp',
    'cintex-wireless-tablet': 'cintex-wireless-free-tablet',
    'foxxd-t8-tablet': 'foxxd-t8-tablet-from-the-government',
    'maxwest-astro-8r': 'maxwest-astro-8r-tablet-free-government',
    'x-mobile-tablet': 'x-mobile-government-tablet',
    'qlink-scepter-8': 'qlink-scepter-8-tablet',
    'lte-wireless-tablet': 'lte-wireless-free-tablet',
    'truconnect-tablet': 'truconnect-free-tablet',
    'texas-tablet-program': 'texas-free-tablet-program',
    'go-md-usa-tablet': 'go-md-usa-free-tablet',
    'verizon-tablet': 'verizon-free-tablet',
    'newphone-wireless-tablet': 'newphone-wireless-free-tablet',
    'free-samsung-tablet': 'free-samsung-tablet',
    'go-tech-management-tablet': 'go-technology-management-free-tablet',
    'assurance-wireless-tablet': 'assurance-wireless-free-government-tablet',
    'standup-wireless-tablet': 'standup-wireless-free-tablet',
    'tmobile-tablet-ebt': 't-mobile-free-tablet-ebt',
    'tablet-snap-benefits': 'free-tablet-with-snap-benefits',
    'free-government-tablet': 'free-government-tablet',
    'moxee-tablet': 'free-moxee-tablet',
    'sky-devices-government': 'free-sky-devices-government-tablet',
    'boost-mobile-tablet': 'boost-mobile-free-tablet',
    'techowl-tablet': 'techowl-free-tablet',
    'cathect-communications': 'cathect-communications-free-tablet',
    'comlink-tablet': 'comlink-free-tablet',
    'nuu-mobile-tablet': 'nuu-mobile-free-tablet',
    'moolah-wireless-tablet': 'moolah-wireless-tablet',
    # Additional mappings for other tablet links
    'acp-free-tablet': 'acp-free-tablet',
    'tablet-with-medicaid': 'free-tablet-with-medicaid',
    'free-tablets-for-seniors': 'free-tablets-for-seniors',
    't-mobile-free-tablet': 't-mobile-free-tablet',
    'sano-health-tablet': 'sano-health-tablet',
    'skyway-wireless-tablet': 'skyway-wireless-tablet',
    'easy-wireless-tablet': 'easy-wireless-tablet',
    'culture-wireless-tablet': 'culture-wireless-tablet',
    'tablet-with-ssi': 'tablet-with-ssi',
    'tablets-for-low-income': 'tablets-for-low-income',
    'tablets-for-students': 'tablets-for-students',
    'tablets-for-disabled': 'tablets-for-disabled',
    'tablet-in-florida': 'tablet-in-florida',
    'tablet-in-texas': 'tablet-in-texas',
    'tablet-in-california': 'tablet-in-california',
    'tablet-in-georgia': 'tablet-in-georgia',
    'track-your-tablet': 'track-your-tablet',
    'acp-tablet-status': 'acp-tablet-status',
}

# Replace each URL
for old_slug, new_slug in url_corrections.items():
    old_url = f'https://world-wire.com/{old_slug}/?utm_source=iphone_portal&utm_medium=tablet_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal'
    new_url = f'https://world-wire.com/{new_slug}/?utm_source=iphone_portal&utm_medium=tablet_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal'
    content = content.replace(old_url, new_url)

# Write the updated content back
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'w') as f:
    f.write(content)

print("✓ Updated all tablet button URLs to correct world-wire.com paths")
