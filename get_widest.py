import requests
import re
from PIL import Image
from io import BytesIO

headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get('https://tenor.com/search/1080p-anime-gifs', headers=headers).text
links = re.findall(r'href="(/view/[^"]+)"', html)
links = list(set(links))

largest_gif = None
max_width = 0
best_content = None

for link in links[:15]:
    try:
        page_html = requests.get('https://tenor.com' + link, headers=headers).text
        gif_match = re.search(r'content="(https://media\.tenor\.com/[^"]+?\.gif)"', page_html)
        if gif_match:
            gif_url = gif_match.group(1)
            r = requests.get(gif_url)
            img = Image.open(BytesIO(r.content))
            width = img.size[0]
            print(f"Checked {gif_url} | Width: {width}px | Size: {len(r.content)}")
            
            if width > max_width:
                max_width = width
                largest_gif = gif_url
                best_content = r.content
    except Exception as e:
        print("Error:", e)

if best_content:
    with open('net_banner.gif', 'wb') as f:
        f.write(best_content)
    print(f"\nSaved largest GIF: {largest_gif} with width {max_width}px!")
