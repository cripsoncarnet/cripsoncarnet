import requests
import re

headers = {'User-Agent': 'Mozilla/5.0'}
html = requests.get('https://tenor.com/search/1080p-anime-gifs', headers=headers).text

# Find GIF links
links = re.findall(r'href="(/view/[^"]+)"', html)
print(f"Found {len(links)} links")

for link in links[:5]:
    try:
        page_html = requests.get('https://tenor.com' + link, headers=headers).text
        gif_match = re.search(r'content="(https://media\.tenor\.com/[^"]+?\.gif)"', page_html)
        if gif_match:
            gif_url = gif_match.group(1)
            r = requests.head(gif_url)
            size = int(r.headers.get('content-length', 0))
            if size > 3000000: # 3MB+ is likely HD
                print(f"HD GIF: {gif_url} | Size: {size}")
                # Save it as net_banner.gif
                r_get = requests.get(gif_url)
                with open('net_banner.gif', 'wb') as f:
                    f.write(r_get.content)
                print("Saved net_banner.gif")
                exit(0)
    except:
        pass
