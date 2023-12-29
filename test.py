#!/usr/bin/python3
# 20231228 檢查比特幣位置餘額

import requests

def get_bitcoin_balance(address):
    base_url = 'https://blockchain.info/q/addressbalance/'
    url = base_url + address
    response = requests.get(url)
    if response.status_code == 200:
        balance = int(response.text)
        return balance
    else:
        print("Failed to retrieve balance. Status code:", response.status_code)
        return None

def main():
    bitcoin_address = "bc1qxhmdufsvnuaaaer4ynz88fspdsxq2h9e9cetdj"
    balance = get_bitcoin_balance(bitcoin_address)

    if balance is not None:
            formatted_balance = "{:.3f}".format(balance / 100000000)  # 將聰轉換為比特幣，留下小數點後三位
    print(formatted_balance)

if __name__ == "__main__":
    main()
