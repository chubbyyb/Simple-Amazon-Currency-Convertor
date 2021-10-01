from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

#if __name__ == '__main__':
def main():

    #   Price
    url = input('Enter your URL: ')
    apikey = '' # PUT APIKEY HERE
    try:
        page = urlopen(url)
    except:
        print("Error opening the URL")
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})
    GBPprice = content.text
    GBPprice = GBPprice[1:]

    #   Name
    content = soup.find('span', {'class': 'a-size-large product-title-word-break'})
    name = content.text.strip()

    #   Conversion
    conversion_rate = urlopen('https://free.currconv.com/api/v7/convert?q=GBP_EUR&compact=ultra&apiKey='+apikey)   # GBP TO EURO API
    data = json.load(conversion_rate)
    conversion_rate = data['GBP_EUR']   # Conversion rate
    finalPrice = round(float(GBPprice) * float(conversion_rate), 2)  # Apply conversion rate
    print('______________________________________________\n' + 'Name: ' + str(name) + '\nGBP Price: £' + str(GBPprice) +
          '\nEUR Price: €' + str(finalPrice) + '\n ______________________________________________')

while True:
    main()
