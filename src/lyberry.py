

import requests

from urllib.parse import urljoin, unquote
from pathlib      import Path
from bs4          import BeautifulSoup


# Config
MUSIC_PATH = Path.home() / "Music" / "Lyberry" # Change this as needed
URL        = "https://files.lyberry.com/audio/sounds/"

def explore(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    listing = soup.find('div', class_='listing')
    if not listing:
        return []
    links = []
    for row in listing.find_all('tr', class_='file'):
        link_tag = row.find('a', href=True)
        if not link_tag:
            continue
        name = link_tag.text.strip()
        href = link_tag['href']
        if 'goup' in link_tag.get('class', []) or name == 'Go up':
            continue
        new_url = urljoin(url, href)
        if name.endswith('/'):
            links.extend(explore(new_url))
        else:
            links.append(new_url)
    return links

def download(links):
    for link in links:
        rel_path = unquote(link.replace(URL, ""))
        local_path = MUSIC_PATH / rel_path
        local_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            response = requests.get(link, stream=True)
            response.raise_for_status()
            with open(local_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded {link}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")

def main():
    links = explore(URL)
    download(links)

if __name__ == "__main__":
    main()