from bs4 import BeautifulSoup as Bs4
import requests

import vnbanks
import vnbanks.base


VIETINBANK_URL = 'https://www.vietinbank.vn/web/home/vn/index.html'
PERIOD = ['NONE',
          'UNDER_ONE_MONTH',
          'UNDER_TWO_MONTHS',
          'UNDER_THREE_MONTHS',
          'UNDER_SIX_MONTHS',
          'UNDER_NINE_MONTHS',
          'UNDER_TWELVE_MONTHS'
          ]

          
class Vietin(vnbanks.base.Bank):
    def __init__(self, name='VietinBank'):
        self.name = name
        self.r = requests.get(VIETINBANK_URL)

    def deposit_rate(self):
        rate = vnbanks.base.Rate('VND')
        rates = self._get_rates()
        rate.rates = dict(zip(PERIOD, rates))
        return rate

    def _get_rates(self):
        soup = Bs4(self.r.text, 'html.parser')
        table = soup.find('table', attrs={'style': "width: 213px"})
        tds = table.findAll('td')
        target = [tds[i].text for i in range(len(tds)) if i%2 != 0]
        return [float(i.replace(',', '.')) for i in target]
