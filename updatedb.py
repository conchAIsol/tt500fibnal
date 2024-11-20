import sqlite3
import requests

url = "https://feed-api.cielo.finance/api/v1/6nhskL8RVpXzWXC7mcC1UXpe3ze2p6P6og1jXVGUW88s/pnl/total-stats?chains=solana&timeframe=7d"

headers = {"accept": "application/json",
           "X-API-KEY": "e18324d3-1b4f-49ee-a797-1e3414c08541"}

response = requests.get(url, headers=headers)

print(response.text)

def insert_wallet(wallet, thirtyday, sevenday, oneday, thirtywinrate):

    conn = sqlite3.connect('wallet_database.db')
    cursor = conn.cursor()

