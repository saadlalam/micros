import requests
from bs4 import BeautifulSoup as bs
'''
A small scrapper to get currency live prices. (it works for other tickers,
just needs a small tweak)
Author :Saadlalam
Contact : saad.lalaoui.lamdegheri@gmail.com 
--------
This is for educational purpose only. 
Please note that it is illegal to spam requests if the web app does not allow so.
'''
URL = "https://finance.google.com/finance?q="

def live_quotes(quote, base):
    
    result = dict()
    page = requests.get(URL+base+quote)
    data = page.content
    s = bs(data, 'html.parser')
    s = s.find('span', attrs={'class': 'bld'})
    s = s.text.split(' ')

    result = {
        'base' : base.upper(),
        'quote': quote.upper(),
        'bid': s[0]
    }
    return result
#WHOOAA ! Unlike Javascript, this Python object above doesn't raise any circular structure error ;)

#Usage :
#print(live_quotes('usd','eur'))
