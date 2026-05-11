import os
import re
import time

templates_dir = r'c:\Users\user\OneDrive\Desktop\kodnest html\DjangoPro\vegelight\delivery\Templates'

for filename in os.listdir(templates_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove the previous mistake where I put ?v= inside the static string
        content = re.sub(r'\'css/style\.css\?v=\d+\'', '\'css/style.css\'', content)
        
        # Also clean up any ?v= already present outside the tag to prevent duplicates
        content = re.sub(r'\{% static \'css/style\.css\' %\}\?v=\d+', '{% static \'css/style.css\' %}', content)
        
        v = int(time.time())
        # Append ?v=v OUTSIDE the tag
        new_content = content.replace('{% static \'css/style.css\' %}\"', f'{{% static \'css/style.css\' %}}?v={v}\"')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Fixed {filename}')
