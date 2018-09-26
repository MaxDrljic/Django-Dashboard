from django.shortcuts import render

# Create your views here.
import requests
# additional functionality for requests package to disable warnings
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup


def scrape():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}
    url = 'https://www.theonion.com/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")
    # columns variable finds the div with a specific class on theonion.com
    columns = soup.find_all(
        'div', {'class': 'curation-module__zone'})
    print(len(columns))


scrape()
