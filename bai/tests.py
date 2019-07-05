from datetime import datetime


from django.test import TestCase

# Create your tests here.
import requests

def checkip(ip):

    URL = 'http://ip.taobao.com/service/getIpInfo.php'
    try:
        r = requests.get(URL, params=ip, timeout=3)
    except requests.RequestException as e:
        print(e)
    else:
        json_data = r.json()
        if json_data[u'code'] == 0:
            print ('所在国家： ' + json_data[u'data'][u'country'])
            print ('所在地区： ' + json_data[u'data'][u'area'])
            print ('所在省份： ' + json_data[u'data'][u'region'])
            print ('所在城市： ' + json_data[u'data'][u'city'])
            print ('所属运营商：' + json_data[u'data'][u'isp'])
        else:
            print ('查询失败,请稍后再试！')

ip={'ip': '202.102.193.68'}
checkip(ip)