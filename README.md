## 

Live currency fetcher is a micro script that scraps google finance page and retrieves live prices of a given currency/currency
---------------------------------------------------------------------------------------------------------------------
### curr_prices

A one function tool to scrap live currency prices directly from google finance page.
-In the example below, we are retrieving the price of EUR based on the current USD value.
Importations:

- requests
- Beautifulsoop

Arguments:
1. Quote : str
2. Base : str

Return:

A dict object :
{
"base": Base,
"quote": Quote,
"bid": Price at bid
}

Usage example:

call:
live_quotes('eur','usd')

result:
{'base': 'usd', 'quote': 'eur', 'bid': '0.8327'}


----------------------------------------------------------------------------------------------
