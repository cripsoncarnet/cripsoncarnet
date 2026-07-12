import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36'}
try:
    html = requests.get('https://wallpapercave.com/anime-scenery-gifs', headers=headers).text
    urls = set(re.findall(r'/wp/[A-Za-z0-9]+\.gif', html))
    print(f"Found {len(urls)} GIF URLs on WallpaperCave.")
    for u in list(urls)[:5]:
        gif_url = 'https://wallpapercave.com' + u
        r = requests.get(gif_url, headers=headers)
        size = len(r.content)
        print(f"Downloaded {gif_url}: {size} bytes")
        if size > 1000000: # Over 1MB means it's a high res banner!
            with open('big_banner.gif', 'wb') as f:
                f.write(r.content)
            print("Successfully saved big_banner.gif!")
            break
except Exception as e:
    print(f"Error: {e}")
