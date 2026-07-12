import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36'}
html = requests.get('https://tenor.com/search/anime-scenery-gifs', headers=headers).text

page_urls = set(re.findall(r'(/view/[^"<>]+?-\d+)', html))
for p in list(page_urls)[:5]:
    try:
        page_html = requests.get('https://tenor.com' + p, headers=headers).text
        match = re.search(r'<meta content="(https://media\.tenor\.com/[^"]+?\.gif)" property="og:image"', page_html)
        if match:
            gif_url = match.group(1)
            print("Found high-res:", gif_url)
            r = requests.get(gif_url, headers=headers)
            size = len(r.content)
            print("Size:", size)
            if size > 1000000: # We want a big one, at least 1MB
                with open("big_banner.gif", "wb") as f:
                    f.write(r.content)
                print("Saved big_banner.gif!")
                break
    except Exception as e:
        print(e)
