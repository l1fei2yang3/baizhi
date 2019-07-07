import random
import time
from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from aliyunsdkcore import client
from aliyunsdkafs.request.v20180112 import AuthenticateSigRequest
from aliyunsdkcore.profile import region_provider

# Create your views here.
from lxml import etree

from bai import checkIP
import redis
from .models import *
from django.utils import timezone

r = redis.Redis(host='192.168.17.128', port=7000)

lxcsdn = ["https://blog.csdn.net/weixin_43582101/column/info/33034",
          "https://blog.csdn.net/weixin_43582101/article/details/86563910",
          "https://blog.csdn.net/weixin_43582101/article/details/86567367",
          ]
'''设置请求头和访问间隔'''
ips = [None]      #存储客户端最后一次访问的ip地址   空列表也是列表,None类型只有None一个值
## ips=[None] 为了防止 list index out of range
last = 0           #存储客服端最后一次访问时间
def isCraw(fun):
    def wrapper(*args,**kwargs):
        global ips,last       #声明全局变量
               #request.META 是一个字典,包含了所有本次HTTP请求的Header信息
        agent = args[0].META.get('HTTP_USER_AGENT') #获取请求头部信息
        print(agent)
        if 'Mozilla' not in agent and 'Safari' not in agent and 'Chrome'not in agent:
            # return HttpResponse(random.choice(lxcsdn))
            return HttpResponse('你的浏览器不对啊！')
        else:
            ip = args[0].META.get('REMOTE_ADDR') #客户端IP地址
            print(ip)
# 什么是remote_addr:
# remote_addr 是服务端根据请求TCP包的ip指定的。假设从client到server中间没有任何代理,
# 那么web服务器（Nginx,Apache等）就会把client的IP设为IPremote_addr；
# 如果存在代理转发HTTP请求,web服务器会把最后一次代理服务器的IP设置为remote_addr
            now = time.time()
            if r.get(ip):
                return HttpResponse("你对发生的事感到好奇吗?如果你仔细读这句话，你就会知道发生了什么事。所以页面没有找到，但是你没有找到它! " )
            elif ip==ips[0] and now-last<2:            #为了防止误伤
                r.set(ip,'1',ex=3600 * 3)
                return HttpResponse("你对发生的事感到好奇吗?如果你仔细读这句话，你就会知道发生了什么事。所以页面没有找到，但是你没有找到它! " )
            last = now
            ips.pop()
            ips.append(ip)
            return fun(*args,**kwargs)
    return wrapper


# 自定义的函数，不是视图
def change_info(func):  # 修改网站访问量和访问ip等信息
    def inner(request,*args, **kwargs):
    # 每一次访问，网站总访问次数加一
        count_nums = BaiVisitnumber.objects.filter(id=1)
        if count_nums:
            count_nums = count_nums[0]
            count_nums.count += 1
        else:
            count_nums = BaiVisitnumber()
            count_nums.count = 1
        count_nums.save()
        print(request.META)
        # 记录访问ip和每个ip的次数
        if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
            client_ip = request.META['HTTP_X_FORWARDED_FOR']
            client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
        else:
            client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
        d_client_ip={'ip': client_ip}

        ip_exist = TUserip.objects.filter(ip=str(client_ip))
        if ip_exist:  # 判断是否存在该ip
            uobj = ip_exist[0]
            try:
                uobj.country = checkIP.checkip(d_client_ip)[0]
                uobj.province = checkIP.checkip(d_client_ip)[1]
                uobj.city = checkIP.checkip(d_client_ip)[2]
                uobj.operator = checkIP.checkip(d_client_ip)[3]
            except:
                uobj.country = 'XX'
                uobj.province = 'XX'
                uobj.city = '内网IP'
                uobj.operator = '内网IP'
            uobj.create_times=timezone.datetime.now()
            uobj.count += 1
        else:
            uobj = TUserip()
            uobj.ip = client_ip
            try:
                uobj.country=checkIP.checkip(d_client_ip)[0]
                uobj.province=checkIP.checkip(d_client_ip)[1]
                uobj.city=checkIP.checkip(d_client_ip)[2]
                uobj.operator=checkIP.checkip(d_client_ip)[3]
            except:
                uobj.country = 'XX'
                uobj.province = 'XX'
                uobj.city = '内网IP'
                uobj.operator = '内网IP'
            uobj.create_times = timezone.datetime.now()
            uobj.count = 1
        uobj.save()

        # 增加今日访问次数
        date = datetime.now()
        today = BaiDaynumber.objects.filter(day=date)
        if today:
            temp = today[0]
            temp.count += 1
        else:
            temp = BaiDaynumber()
            temp.day = date
            temp.count = 1
        temp.save()
        return func(request,*args, **kwargs)
    return inner
# @change_info
# def zhuang(i):
#     return i
# @change_info
# @isCraw
def index(request):
    status = request.session.get("login")  # 获取登录状态
     #当网站被访问时，更新网站访问次数
    if status:
        return render(request,'main.html')
    return redirect('baiapp:login')

# @change_info
# @isCraw
def introduce(request):
    return render(request,'introduce.html')

# @change_info
# @isCraw
def mainc(request):
    # try:
        city = request.GET.get('city')  # 城市编码
        job = request.GET.get('job')  # 职业名称
        print(148,city,job)
        cj=request.GET.get('cj')#获取前端传来的下拉框值
        searchtext=request.GET.get('searchtext')#获取前端传来的搜索词
        number = request.GET.get("number")  # 获取前端传来的页码
        if not number:  # 判断如果页面为空的话
            number = 1  # 页码的值默认为1
        if city=='None' and job=='None':
            # select = TPersonalInformation.objects.filter(jobsite__icontains=city, expect_job__icontains=job)
            select = TPersonalInformation.objects.all()
        elif city:
            select = TPersonalInformation.objects.filter(jobsite__icontains=city, expect_job__icontains=job)
        elif cj=='城市':
            select = TPersonalInformation.objects.filter(jobsite__icontains=searchtext)
        elif cj=='职位':
            select = TPersonalInformation.objects.filter(expect_job__icontains=searchtext)
        elif cj=='--请选择--':
            if searchtext in '北京':
                select = TPersonalInformation.objects.filter(jobsite__icontains=searchtext)
            elif searchtext in '上海':
                select=TPersonalInformation.objects.filter(jobsite__icontains=searchtext)
            elif searchtext in '广州':
                select=TPersonalInformation.objects.filter(jobsite__icontains=searchtext)
            elif searchtext in '深圳':
                select=TPersonalInformation.objects.filter(jobsite__icontains=searchtext)
            elif searchtext in '平面设计':
                select=TPersonalInformation.objects.filter(expect_job__icontains=searchtext)
            elif searchtext in '软件工程师':
                select=TPersonalInformation.objects.filter(expect_job__icontains=searchtext)
            elif searchtext in 'Java开发工程师':
                select=TPersonalInformation.objects.filter(expect_job__icontains=searchtext)
            elif searchtext in '软件测试':
                select=TPersonalInformation.objects.filter(expect_job__icontains=searchtext)
        elif not searchtext:
            select = TPersonalInformation.objects.all().order_by("id")

        else:
            return HttpResponse('您输入的查询不到')
        print(select)
        beijing=TPersonalInformation.objects.filter(jobsite='北京').count()
        shanghai=TPersonalInformation.objects.filter(jobsite='上海').count()
        guangzhou=TPersonalInformation.objects.filter(jobsite='广州').count()
        shenzhen=TPersonalInformation.objects.filter(jobsite='深圳').count()
        pagtor = Paginator(select, per_page=10)  # 将查询到的数据进行每一页30条数据划分
        page = pagtor.page(number)
        print(178,page,number)
        return render(request,'menu.html',{'select':select,'page':page,'number':number,'city':city,'job':job,'beijing':beijing,'guangzhou':guangzhou,'shanghai':shanghai,'shenzhen':shenzhen})
    # except:
    #     return HttpResponse('页码不正确')
# @change_info
# @isCraw
# def menu(request):
#     # try:
#         city=request.GET.get('city')#城市编码
#         job=request.GET.get('job')#职业名称
#         print(city,job)
#         number = request.GET.get("number")  # 获取前端传来的页码
#         if not number:  # 判断如果页面为空的话
#             number = 1  # 页码的值默认为1
#         select = TPersonalInformation.objects.filter(jobsite__icontains=city,expect_job__icontains=job)
#         pagtor = Paginator(select, per_page=30)  # 将查询到的数据进行每一页30条数据划分
#         page=pagtor.page(number)
#         return render(request,'menu.html',{'select':select,'page':page,'number':number,})
#     # except:
#     #     return HttpResponse('页码不正确')
def login(request):
    return render(request,'login.html')
def loginlogic(request):
    username=request.POST.get('username')
    psw=request.POST.get('psw')
    check=TUser.objects.filter(username=username,pass_field=psw)
    code=request.session.get('code')
    if check:
        request.session["login"] = "ok"
        if code=='100':
            return redirect('baiapp:index')
        else:
            return redirect('baiapp:login')
    else:
        return redirect('baiapp:login')
def register(request):
    return render(request,'register.html')
def registerlogic(request):
    username=request.POST.get('username') #用户名
    usrtel=request.POST.get('usrtel') #手机号
    email=request.POST.get('email') #电子邮件
    psw=request.POST.get('psw') #密码
    print(username,usrtel,email,psw)
    try:
        if username and usrtel and email and psw:
            if TUser.objects.filter(username=username):
                return ('账号已经存在')
            else:
                insert=TUser.objects.create(username=username,pass_field=psw,phone=usrtel,email=email)
                return redirect('baiapp:login')
        else:
            return HttpResponse('不能为空')
    except:
        return redirect('baiapp:register')
def checkName(request):
    username = request.GET.get("username")
    result=TUser.objects.filter(username=username)
    if result:
        return HttpResponse("1")
    else:
        return HttpResponse('0')

def huakuai(req):    #登录滑块验证
    sessionid = req.GET.get('csessionid')
    sig = req.GET.get('sig')
    token = req.GET.get('nc_token')
    # print(sig)
    # print(sessionid)
    # print(token)
    region_provider.add_endpoint('afs', 'cn-hangzhou', 'afs.aliyuncs.com')

    # YOUR ACCESS_KEY、YOUR ACCESS_SECRET请替换成您的阿里云accesskey id和secret
    clt = client.AcsClient('LTAI1Hv1XFlpUX3z', 'Oo49pDCa8jFRJkGZHI2iKqiS8DIxKK', 'cn-hangzhou')
    request = AuthenticateSigRequest.AuthenticateSigRequest()


    #必填参数：从前端获取，不可更改，android和ios只传这个参数即可
    request.set_SessionId(sessionid)
    #必填参数：从前端获取，不可更改
    request.set_Sig(sig)
    #必填参数：从前端获取，不可更改
    request.set_Token(token)
    #必填参数：从前端获取，不可更改
    request.set_Scene('nc_login')
    #必填参数：后端填写
    request.set_AppKey('FFFF0N00000000007F79')
    #必填参数：后端填写
    request.set_RemoteIp('192.168.17.1')

    result = clt.do_action(request)#返回code 100表示验签通过，900表示验签失败
    print(result)
    html = etree.HTML(result)
    code = html.xpath('//code/text()')[0]
    # print(code)
    req.session['code'] = code
    return HttpResponse('%s'%code)
def tst(request):
    return render(request,'test.html')