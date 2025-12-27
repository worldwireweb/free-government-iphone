
import os
import re

def update_footer(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, "r") as f:
        content = f.read()

    # Check if sitemap is already there
    if 'href="sitemap.xml"' in content:
        print(f"Sitemap link already exists in {filepath}")
        return

    # Regex to find the privacy policy link
    # It might span multiple lines or have different styles
    # We look for <a href="privacy-policy.html" ... >...</a>
    # We want to insert the sitemap link after it.
    
    # This regex tries to capture the whole anchor tag for privacy policy
    # pattern: (<a\s+[^>]*href=["']privacy-policy\.html["'][^>]*>.*?</a>)
    # flag re.DOTALL is important
    
    pattern = r'(<a\s+[^>]*href=["\']privacy-policy\.html["\'][^>]*>.*?</a>)'
    
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        privacy_link = match.group(1)
        
        # Extract style from privacy link to reuse
        style_match = re.search(r'style=["\'](.*?)["\']', privacy_link)
        style = style_match.group(1) if style_match else ""
        
        # Create sitemap link
        # We assume the footer links are typically separated by whitespace or newlines
        sitemap_link = f'\n            <a href="sitemap.xml" style="{style}">Sitemap</a>'
        
        # Insert
        new_content = content[:match.end()] + sitemap_link + content[match.end():]
        
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Privacy policy link not found in {filepath}")

files_to_update = [
    "free-government-iphone.html",
    "free-government-samsung-phone.html",
    "free-government-tablet.html",
    "free-government-laptop.html",
    "free-government-5g-phone.html",
    "about.html",
    "contact.html",
    "privacy-policy.html",
    "tablets.html" 
]

for file in files_to_update:
    update_footer(file)
