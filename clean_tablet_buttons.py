#!/usr/bin/env python3
"""
Script to keep ONLY the 70 URLs specified by the user and remove all other tablet buttons
"""

# Read the tablet HTML file
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'r') as f:
    content = f.read()

# The EXACT 70 URLs the user wants to keep (without UTM parameters)
urls_to_keep = [
    'free-tablet-with-food-stamps-florida',
    'gen-mobile-free-tablet',
    'maxsip-telecom-free-tablet',
    'windstream-ebb-tablet-free',
    'unity-wireless-free-tablet',
    'free-5g-government-tablet',
    'vortex-government-phones-and-tablets',
    'public-wireless-free-tablet-program',
    'get-free-tablets-with-food-stamps-ebt-card',
    'q-link-wireless-free-tablet',
    'free-tablets-for-veterans',
    'excess-telecom-free-tablet',
    'm8l-tablet-free-government',
    'sky-devices-elite-t8-tablet',
    'free-government-tablet-in-california',
    'free-government-tablet-florida',
    'safelink-free-tablet',
    'whoop-connect-free-tablet',
    'cellution-free-tablet',
    'vortex-tab-8-4g-tablet-for-free',
    'free-tablet-with-phone-from-government',
    'reset-maxsip-telecom-tablet',
    'free-tablet-for-disabled',
    'free-maxwest-nitro-8-tablet',
    'wrazzle-wireless-free-tablet',
    'metropcs-free-tablet',
    'grandpad-tablet-for-seniors',
    'wireless-now-free-tablet',
    '10-dollar-tablet-from-government',
    'acp-free-tablet-near-me',
    'free-tablet-with-ebt-georgia',
    'tone-communication-free-tablet',
    'free-tablet-with-ebt-card',
    'hoop-wireless-free-tablet',
    'att-free-tablet',
    'emergency-broadband-benefit-free-tablet',
    't-mobile-free-tablet-for-seniors',
    'airtalk-wireless-free-tablet',
    'torch-wireless-free-tablet',
    'cloud-mobile-tablet-free',
    'city-communications-free-tablets',
    'u2-connect-free-tablet',
    'how-do-i-get-100-off-a-tablet-with-acp',
    'cintex-wireless-free-tablet',
    'foxxd-t8-tablet-from-the-government',
    'maxwest-astro-8r-tablet-free-government',
    'x-mobile-government-tablet',
    'qlink-scepter-8-tablet',
    'lte-wireless-free-tablet',
    'truconnect-free-tablet',
    'texas-free-tablet-program',
    'go-md-usa-free-tablet',
    'verizon-free-tablet',
    'newphone-wireless-free-tablet',
    'free-samsung-tablet',
    'go-technology-management-free-tablet',
    'assurance-wireless-free-government-tablet',
    'standup-wireless-free-tablet',
    't-mobile-free-tablet-ebt',
    'free-tablet-with-snap-benefits',
    'free-government-tablet',
    'free-moxee-tablet',
    'free-sky-devices-government-tablet',
    'boost-mobile-free-tablet',
    'techowl-free-tablet',
    'cathect-communications-free-tablet',
    'comlink-free-tablet',
    'nuu-mobile-free-tablet',
    'moolah-wireless-tablet',
]

# Build the new button section with ONLY these 70 URLs
new_buttons = []
for slug in urls_to_keep:
    url = f'https://world-wire.com/{slug}/?utm_source=iphone_portal&utm_medium=tablet_page&utm_campaign=organic_traffic&utm_term=Github&utm_content=vishal'
    # Create readable button text from slug
    text = slug.replace('-', ' ').title()
    new_buttons.append(f'            <a href="{url}" class="model-pill">{text}</a>')

# Find the tablets-list section and replace it
import re

# Pattern to match the entire model-grid div within tablets-list section
pattern = r'(<section id="tablets-list".*?<div class="model-grid">)(.*?)(</div>\s*</section>)'

replacement_buttons = '\n'.join(new_buttons)
replacement = r'\1\n' + replacement_buttons + r'\n        \3'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the updated content back
with open('/Users/macos/free-government-iPhone-11/free-government-iphone/free-government-tablet.html', 'w') as f:
    f.write(content)

print(f"✓ Updated tablet page to show ONLY the {len(urls_to_keep)} specified URLs")
print(f"✓ Removed all other buttons that were redirecting to homepage")
