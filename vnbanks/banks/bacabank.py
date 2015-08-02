"""Lai suat tiet kiem Ngan hang Bac A."""
from bs4 import BeautifulSoup as Bs4
import requests

import vnbanks
import vnbanks.base

BAC_A_BANK = 'http://www.baca-bank.vn/chuyen-muc/77/lai-suat-tiet-kiem'


class Bacabank(vnbanks.base.Bank):
    """."""
    def __init__(self, name='BacABank'):
        """."""
        self.name = name
        self.r = requests.get(BAC_A_BANK)

    def deposit_rate(self):
        rate = vnbanks.base.Rate('VND')
        PERIOD = ['NONE',
                  '1_WEEK',
                  '2_WEEK',
                  '3_WEEK',
                  '1_MONTH',
                  '2_MONTHS',
                  '3_MONTHS',
                  '4_MONTHS',
                  '5_MONTHS',
                  '6_MONTHS',
                  '7_MONTHS',
                  '8_MONTHS',
                  '9_MONTHS',
                  '10_MONTHS',
                  '11_MONTHS',
                  '12_MONTHS',
                  '13_MONTHS',
                  '15_MONTHS',
                  '18_MONTHS'
                  ]
        rates = self._get_rates()
        rate.rates = dict(zip(PERIOD, rates))
        return rate

    def _get_rates(self):
        soup = Bs4(self.r.text, 'html.parser')
        table = soup.findAll('table')[1]
        tds = table.findAll(
           'td',
           {"style": "width: 116px; padding-left: 10px; text-align: center; "})
        target = [tds[i].string for i in range(2,len(tds),3)]
        return [float(i.replace(',', '.')) for i in target]
