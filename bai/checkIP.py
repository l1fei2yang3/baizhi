import json

import requests



def checkip(ip):

    URL = 'http://ip.taobao.com/service/getIpInfo.php'
    try:
        r = requests.get(URL, params=ip).text
        # print(r)
    except :
        # requests.RequestException as e
        # print(e)
        pass
    else:
        json_data = json.loads(r)
        if json_data[u'code'] == 0:
            country=json_data[u'data'][u'country']
            # province='所在地区： ' + json_data[u'data'][u'area']
            province=json_data[u'data'][u'region']
            city=json_data[u'data'][u'city']
            operator=json_data[u'data'][u'isp']
            return country, province, city, operator
        else:
            return ('查询失败,请稍后再试！')

# ip={'ip': '202.102.193.68'}
# ip={'ip': '127.0.0.1'}
# TUserip.objects.create(ip=ip,country=checkip(ip)[0])
# print(checkip(ip))