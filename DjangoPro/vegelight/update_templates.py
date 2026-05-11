import os

templates_dir = r'c:\Users\user\OneDrive\Desktop\kodnest html\DjangoPro\vegelight\delivery\Templates'

for filename in os.listdir(templates_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '{% load static %}' not in content:
            new_content = content.replace('</head>', '    {% load static %}\n    <link href="{% static \'css/style.css\' %}" rel="stylesheet">\n</head>')
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filename}')
        elif '{% static \'css/style.css\' %}' not in content:
            new_content = content.replace('</head>', '    <link href="{% static \'css/style.css\' %}" rel="stylesheet">\n</head>')
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {filename}')
