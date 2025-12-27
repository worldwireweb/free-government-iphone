
import os
import re

# We will manually define the tablet_items here to ensure we capture exactly what is in the generator script
# Or better, we can read the file and extract the list, but manual definition based on the user's provided list + filenames is consistent.
# Actually, I will read generate_blog_content.py to be 100% sure I use the same filenames.

def get_tablet_items():
    # Helper to parse the python file and extract the tablet_items list
    # This is a bit hacky but safer than assuming
    items = []
    with open("generate_blog_content.py", "r") as f:
        content = f.read()
        
    # Regex to find tablet_items list
    # Look for tablet_items = [ ... ]
    match = re.search(r'tablet_items\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if match:
        list_str = match.group(1)
        # Each item is a dict, let's parse them
        # We can use eval on the list string if it's safe (it is, it's my own file)
        # cleaning up the string to be a valid list
        list_content = "[" + list_str + "]"
        try:
            items = eval(list_content)
        except Exception as e:
            print(f"Error parsing list: {e}")
            return []
    return items

def update_html(items):
    html_path = "free-government-tablet.html"
    with open(html_path, "r") as f:
        html = f.read()

    # Generate the new grid HTML
    # <a href="blog/{filename}" class="model-pill">{text}</a>
    grid_html = ""
    for item in items:
        # User requested redirection to external link in the article
        # But for this page, we link to the internal article
        link = f"blog/{item['file']}"
        text = item['text']
        grid_html += f'            <a href="{link}" class="model-pill">{text}</a>\n'

    # Replace the existing model-grid content
    # Look for <div class="model-grid"> ... </div>
    # Uses regex to match the content inside the div
    
    pattern = r'(<section id="tablets-list".*?<div class="model-grid">)(.*?)(</div>)'
    
    # We need to be careful with the regex matching everything inside
    # Using re.DOTALL to match newlines
    
    new_section = r'\1\n' + grid_html + r'        \3'
    
    updated_html = re.sub(pattern, new_section, html, flags=re.DOTALL)
    
    with open(html_path, "w") as f:
        f.write(updated_html)
    
    print(f"Updated {html_path} with {len(items)} items.")

if __name__ == "__main__":
    items = get_tablet_items()
    if items:
        update_html(items)
    else:
        print("No items found.")
