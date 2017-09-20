## Micros

This folder contains microscripts for single task handling.
-----------------------------------------------------------------------------------------
### curr_prices

A one function tool to scrap live currency prices directly from google finance page.

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

>>>live_quotes('eur','usd')

{'base': 'usd', 'quote': 'eur', 'bid': '0.8327'}
----------------------------------------------------------------------------------------------
