from urllib import request
from bs4 import BeautifulSoup

# Header gibberish that I have not investigated - needed otherwise 403 Forbidden...
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}


class GetMyHtml:
    def call_this_url(self, url):
        # Assemble request and add headers where needed
        req = request.Request(url, None, headers=HEADERS)
        resp = request.urlopen(req).read()

        # Turn into beautiful soup and make it pretty
        soup = BeautifulSoup(resp, "html.parser").prettify()
        soup = soup.replace("&quot;", "\"")

        return soup
