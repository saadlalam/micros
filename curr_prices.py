import requests
from bs4 import BeautifulSoup as bs
'''
A small scrapper to get currency live prices. (it works for other tickers,
just needs a small tweak)
Author :Saadlalam
Contact : saad.lalaoui.lamdegheri@gmail.com 
'''
URL = "https://finance.google.com/finance?q="

def live_quotes(quote, base):
    
    result = {}
    page = requests.get(URL+base+'+to+'+quote)
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

#print(live_quotes('usd','eur'))
