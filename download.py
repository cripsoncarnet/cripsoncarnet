import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

urls = [
    ('anime_banner.gif', 'https://media.giphy.com/media/5tsjxsQWgylTW/giphy.gif'),
    ('anime_left.gif', 'https://media.giphy.com/media/l4pTfx2qLs36Uv5m0/giphy.gif'),
    ('anime_right.gif', 'https://media.giphy.com/media/F32551yT5P8z6/giphy.gif')
]

for name, url in urls:
    try:
        r = requests.get(url, headers=headers)
        with open(name, 'wb') as f:
            f.write(r.content)
        print(f"Downloaded {name}: {len(r.content)} bytes")
    except Exception as e:
        print(f"Error {name}: {e}")
