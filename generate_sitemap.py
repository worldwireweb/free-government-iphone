import os
import datetime

# Configuration
BASE_URL = "https://world-wireconnect.com"
ROOT_DIR = "."
SITEMAP_FILE = "sitemap.xml"

def generate_sitemap():
    urlset = []
    
    # Header
    urlset.append('<?xml version="1.0" encoding="UTF-8"?>')
    urlset.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Traverse directory
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                # Get file path relative to root
                rel_path = os.path.relpath(os.path.join(root, file), ROOT_DIR)
                
                # normalize path separators
                rel_path = rel_path.replace(os.sep, '/')
                
                # Construct URL (handle index.html potentially, but for now map 1:1)
                # Usually index.html maps to the root directory, but let's keep it simple for now or strip it if it's the root index.html
                if rel_path == "index.html":
                     url = BASE_URL + "/"
                else:
                    url = f"{BASE_URL}/{rel_path}"

                # Get last modification time
                filepath = os.path.join(root, file)
                mod_time = os.path.getmtime(filepath)
                lastmod = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

                # Create XML entry
                entry = f"""    <url>
        <loc>{url}</loc>
        <lastmod>{lastmod}</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>"""
                urlset.append(entry)

    # Footer
    urlset.append('</urlset>')

    # Write to file
    with open(SITEMAP_FILE, "w") as f:
        f.write("\n".join(urlset))
    
    print(f"Sitemap generated at {os.path.abspath(SITEMAP_FILE)} with {len(urlset)-2} URLs.")

if __name__ == "__main__":
    generate_sitemap()
