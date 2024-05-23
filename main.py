import requests

def geturl(unique):
    return f"https://www.alphavantage.co/query?function={unique}&apikey="



def getdata(url):
    return requests.get(url).json()
    
 


def main():
    global stock
    global apikey
    apikey = open("api_key.txt")
    while True:
        if action =="1":
            stock = input("What Stock do you want to know about?")
            data = getdata(geturl(f"SYMBOL_SEARCH&keywords={stock}"))
            basicdata = {
                "symbol" : data["bestMatches"][0]["1. symbol"],
                "name"   : data["bestMatches"][0]["2. name"],
                "region" : data["bestMatches"][0]["4. region"] }
            price_data = getdata(geturl(f'TIME_SERIES_INTRADAY&{basicdata["symbol"]}=IBM&interval=5min'))
            price = {
                "open"   : price_data["Time Series (5min)"][0]["1. open"],
                "high"   : price_data["Time Series (5min)"][0]["2. high"],
                "low"    : price_data["Time Series (5min)"][0]["3. low"],
                "close"  : price_data["Time Series (5min)"][0]["4. close"] }
            basicdata["price"] = price
            print(basicdata)



action = input("Hello, this is your Personal Stock-Screener.\nFor Information about a Certain Stock Press \'1\'")
main()

