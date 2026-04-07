import os

base_path = '/Users/haider/Desktop/aprilgames/Astray-master/Astray-master'
index_html_path = os.path.join(base_path, 'index.html')
logo_b64_path = os.path.join(base_path, 'alt_logo_b64.txt')

with open(logo_b64_path, 'r') as f:
    logo_b64 = f.read().strip()

with open(index_html_path, 'r') as f:
    content = f.read()

# Update CSS for larger logo
content = content.replace('height: 1.2em;', 'height: 2em;')

# Find the pif-header block and replace it
import re
new_html = f'<div id="pif-header">\n        <img src="data:image/png;base64,{logo_b64}" alt="PIF Logo">\n    </div>'

# Regular expression to catch the block regardless of the specific base64 content
pattern = r'<div id="pif-header">.*?</div>'
content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open(index_html_path, 'w') as f:
    f.write(content)

print("PIF Logo replacement and text removal completed.")
