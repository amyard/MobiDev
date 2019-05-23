import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from mosestokenizer import MosesDetokenizer


def add_trade_mark_sign(string):
    data = [ word+'\N{TRADE MARK SIGN}' if len(word)>5 else word for sent in sent_tokenize(string) for word in word_tokenize(sent) ]
    with MosesDetokenizer() as detokenize:
        res = detokenize(data)
    return res



def crawling(url):
    ua = UserAgent()
    response = requests.get(url, headers= {'User-Agent':str(ua.random)})
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    first_tag = soup.body.findChildren()[0].text
    result = add_trade_mark_sign(first_tag)
    return result


def get_short_url(full_url):
    short_url = '/'.join(full_url.split('/')[3:])
    return short_url