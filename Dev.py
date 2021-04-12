
import requests
from fake_useragent import UserAgent
import urllib.parse

def UrlGen(region, btype='電梯大廈', page=0)->str:
    r = ','.join([urllib.parse.quote(s) for s in region])
    bt = urllib.parse.quote(btype)
    return f'https://buy.yungching.com.tw/region/{r}_c/_rm/{bt}_type/?pg={page}'


ua = UserAgent()
fa_firefox = ua.firefox
test_url = UrlGen(['宜蘭縣-宜蘭市,宜蘭縣-羅東鎮,宜蘭縣-五結鄉'])
r = requests.get(url=test_url,
                 headers = {'User-Agent':fa_firefox})
print(r.status_code)
print(r.text)