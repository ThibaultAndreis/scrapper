import requests
from bs4 import BeautifulSoup


def parse_price(selectedsku):
    r = requests.get('https://www.cdiscount.com/f-0-' + selectedsku + '.html')

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        test = soup.select(".hideFromPro.price")
        if test:
            for variable in test:
                print(variable.attrs.get('content'))
        else:
            print('no product found')

    elif r.status_code == 429:
        print('timed out, try later')

    elif r.status_code == 400:
        print('no page found')

    else:
        print('undocumented error')