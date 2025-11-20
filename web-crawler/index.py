import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def crawl(url):
    if url in visited:
        return
    visited.add(url)

    print("Visiting:", url)

    try:
        r = requests.get(url, timeout=5)
    except Exception as e:
        print("Error:", e)
        return

    soup = BeautifulSoup(r.text, "html.parser")

    # find ALL <a> tags
    links = soup.find_all("a")

    for tag in links:
        href = tag.get("href")
        if not href:
            continue

        # convert relative URLs → absolute URLs
        next_url = urljoin(url, href)

        # skip javascript:, mailto:, etc
        if not next_url.startswith("http"):
            continue

        crawl(next_url)


crawl("http://localhost:3000")
