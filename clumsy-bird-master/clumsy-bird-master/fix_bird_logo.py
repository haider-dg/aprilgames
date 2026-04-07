import os
import re

base_path = '/Users/haider/Desktop/aprilgames/clumsy-bird-master/clumsy-bird-master'
index_html_path = os.path.join(base_path, 'index.html')
logo_b64_path = '/tmp/bird_logo_b64_new.txt'

with open(logo_b64_path, 'r') as f:
    logo_b64 = f.read().strip()

with open(index_html_path, 'r') as f:
    content = f.read()

# Find the pif-header block and replace it
new_html = f'<div id="pif-header">\n        <img src="data:image/png;base64,{logo_b64}" alt="Logo">\n    </div>'
pattern = r'<div id="pif-header">.*?</div>'
content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open(index_html_path, 'w') as f:
    f.write(content)

print("Bird Logo fixed in index.html")
