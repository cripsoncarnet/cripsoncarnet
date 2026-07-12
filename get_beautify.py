import requests
import re
import urllib3
urllib3.disable_warnings()

html = requests.get('https://raw.githubusercontent.com/rzashakeri/beautify-github-profile/master/README.md').text
urls = re.findall(r'(https?://[^\s<>)"]+\.gif)', html)
urls = list(set(urls))

for url in urls:
    if 'anime' in url.lower() or 'scenery' in url.lower() or 'banner' in url.lower() or 'cover' in url.lower():
        print(f"Possible: {url}")

print(f"\nFound {len(urls)} total GIFs.")
# Let's just print the first 15 for manual inspection
for url in urls[:15]:
    print(url)
