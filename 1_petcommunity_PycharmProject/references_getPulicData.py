
import requests
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import xmltodict
import json


result = requests.get('http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?bgnde=20140101&endde=20141231&upkind=417000&pageNo=1&&numOfRows=10000000&ServiceKey=Cs8el%2FuhtlYCY%2BHBBp9jCapmuo%2FmEjVkn0P%2BU6BY78tnS%2BTrPlz7BUEk%2BDfKOvvioI9hcaSuAJT%2FpgGsqAQG9A%3D%3D')
dict_type = xmltodict.parse(result.content)
json_type = json.dumps(dict_type)
dict2_type = json.loads(json_type)
body = dict2_type['response']['body']
items = body['items']

list=[]
list3=[]
for item in items["item"]:

     print(item)