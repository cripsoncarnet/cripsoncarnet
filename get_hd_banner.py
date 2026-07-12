import requests
url = 'https://i.pinimg.com/originals/e8/35/65/e83565e3b610c1f618a804db35824905.gif'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0.0.0 Safari/537.36', 'Referer': 'https://www.pinterest.com/'}
r = requests.get(url, headers=headers)
if r.status_code == 200:
    with open('hd_banner.gif', 'wb') as f:
        f.write(r.content)
    print('Success, size:', len(r.content))
else:
    print('Failed with status:', r.status_code)
