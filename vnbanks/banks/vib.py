import bs4
import requests

import vnbanks
import vnbanks.base


VIB_DEPOSITE_TABLE = 'https://vib.com.vn/1775-truy-cap-nhanh/1781-lai-suat-\
        tiet-kiem/1829-bieu-lai-suat-tiet-kiem-thuong.aspx'


class VIB(vnbanks.base.Bank):
    def __init__(self, name='VIB'):
        self.name = name

    def deposit_rate(self):
        rate = vnbanks.base.Rate('VND')
        rate.rates['ONE_MONTH'] = self._get_1_month_rate()
        rate.rates['THREE_MONTHS'] = 1.5
        rate.rates['TWELVE_MONTHS'] = 2.0
        return rate

    def _get_1_month_rate(self):
        vibhtml = requests.get(VIB_DEPOSITE_TABLE)
        soup = bs4.BeautifulSoup(vibhtml.text, 'html.parser')
        trs = soup.findAll('tr', 'tr_table_interest')
        tr = trs[4]
        target = tr.find('td', {"class": "pad5 fontNorCenter"})
        vn_notation = target.get_text().strip().replace(',', '.')
        return float(vn_notation)
