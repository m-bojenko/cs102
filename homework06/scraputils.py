import requests
import time
from bs4 import BeautifulSoup
from typing import List


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []

    tbl_list = parser.table.findAll('table')
    tr_list = tbl_list[1].findAll('tr')
    for i in range(0, 90, 3):
        new = dict()
        new['author'] = tr_list[i + 1].a.text
        new['points'] = tr_list[i + 1].span.text[:-6]
        comments = tr_list[i + 1].findAll('a')
        new['comments'] = comments[len(comments) - 1].text[:-9]
        if new['comments'] == '':
            new['comments'] = '0'
        new['title'] = tr_list[i].findAll('a')[1].text
        a_mas = List[str]
        a_mas = tr_list[i].findAll('a')
        new['url'] = a_mas[len(a_mas) - 1].text
        if new['url'] == new['title']:
            new['url'] = ''
        news_list.append(new)

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    url = ''
    table = parser.table.find_all('table')[1]
    tr = table.findAll('tr')
    url = url + str(tr[len(tr) - 1].a.get('href'))

    return url


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))

        delay = 2
        max_retries = 5
        backoff_factor = 0.3
        for tryes in range(max_retries):
            try:
                response = requests.get(url)
            except requests.exceptions.RequestException:
                if tryes == max_retries - 1:
                    raise
            else:
                break
            time.sleep(delay)
            delay = backoff_factor * (2 ** tryes)

        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

# news_list = get_news('https://news.ycombinator.com/newest', n_pages=40)
# print(news_list[:34])
