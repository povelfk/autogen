# filename: fetch_abstract.py

import urllib.request
import re

def fetch_abstract(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        abstract = re.search('<blockquote class="abstract mathjax">(.*?)</blockquote>', html, re.DOTALL).group(1)
        abstract = re.sub('<[^<]+?>', '', abstract)  # Remove HTML tags
        return abstract.strip()

url = "https://arxiv.org/abs/2308.08155"
print(fetch_abstract(url))