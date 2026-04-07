import os

base_path = '/Users/haider/Desktop/aprilgames/clumsy-bird-master/clumsy-bird-master'
index_html_path = os.path.join(base_path, 'index.html')
logo_b64_path = '/tmp/bird_logo_b64.txt'

with open(logo_b64_path, 'r') as f:
    logo_data_uri = f.read().strip()

with open(index_html_path, 'r') as f:
    content = f.read()

# Add CSS
style_to_add = f"""
    <style>
        #pif-header {{
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            pointer-events: none; /* Don't interfere with game clicks */
        }}

        #pif-header img {{
            height: 60px;
            width: auto;
            filter: drop-shadow(0 0 10px rgba(0,0,0,0.5));
        }}
    </style>
"""

content = content.replace('</head>', style_to_add + '\n    </head>')

# Add HTML
html_to_add = f"""
    <div id="pif-header">
        <img src="{logo_data_uri}" alt="Logo">
    </div>
"""

content = content.replace('<body>', '<body>\n    ' + html_to_add)

with open(index_html_path, 'w') as f:
    f.write(content)

print("Logo added to Clumsy Bird index.html")
