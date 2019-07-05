from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from bai import checkIP
from bai.models import TUser, TPersonalInformation

from .models import *
from django.utils import timezone


#自定义的函数，不是视图
def change_info(request):  # 修改网站访问量和访问ip等信息
    # 每一次访问，网站总访问次数加一
    count_nums = BaiVisitnumber.objects.filter(id=1)
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = BaiVisitnumber()
        count_nums.count = 1
    count_nums.save()

    # 记录访问ip和每个ip的次数
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    d_client_ip={'ip': client_ip}
    print(d_client_ip)

    ip_exist = TUserip.objects.filter(ip=str(client_ip))
    if ip_exist:  # 判断是否存在该ip
        uobj = ip_exist[0]
        try:
            uobj.country = checkIP.checkip(d_client_ip)[0]
            uobj.province = checkIP.checkip(d_client_ip)[1]
            uobj.city = checkIP.checkip(d_client_ip)[2]
            uobj.operator = checkIP.checkip(d_client_ip)[3]
        except:
            uobj.country = '本地'
            uobj.province = '本地'
            uobj.city = '本地'
            uobj.operator = '本地'
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
            uobj.country = '本地'
            uobj.province = '本地'
            uobj.city = '本地'
            uobj.operator = '本地'
        uobj.create_times = timezone.datetime.now()
        uobj.count = 1
    uobj.save()

    # 增加今日访问次数
    date = timezone.now().date()
    today = BaiDaynumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = BaiDaynumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()

def index(request):
    status = request.session.get("login")  # 获取登录状态
    change_info(request) #当网站被访问时，更新网站访问次数
    if status:
        return render(request,'main.html')
    return redirect('baiapp:login')
def introduce(request):
    change_info(request)  # 当网站被访问时，更新网站访问次数
    return render(request,'introduce.html')
def mainc(request):
    # try:
        cj=request.GET.get('cj')#获取前端传来的下拉框值
        searchtext=request.GET.get('searchtext')#获取前端传来的搜索词
        number = request.GET.get("number")  # 获取前端传来的页码
        if not number:  # 判断如果页面为空的话
            number = 1  # 页码的值默认为1
        if cj=='城市':
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
            select = TPersonalInformation.objects.all()
        else:
            return HttpResponse('您输入的查询不到')
        pagtor = Paginator(select, per_page=30)  # 将查询到的数据进行每一页30条数据划分
        page=pagtor.page(number)
        print(cj,searchtext)


        change_info(request)  # 当网站被访问时，更新网站访问次数
        return render(request,'menu.html',{'select':select,'page':page,'number':number,})
    # except:
    #     return HttpResponse('页码不正确')
def menu(request):
    change_info(request)  # 当网站被访问时，更新网站访问次数
    try:
        city=request.GET.get('city')#城市编码
        job=request.GET.get('job')#职业名称
        print(city,job)
        number = request.GET.get("number")  # 获取前端传来的页码
        if not number:  # 判断如果页面为空的话
            number = 1  # 页码的值默认为1
        select = TPersonalInformation.objects.filter(jobsite=city,expect_job=job)
        pagtor = Paginator(select, per_page=30)  # 将查询到的数据进行每一页30条数据划分
        page=pagtor.page(number)

        return render(request,'menu.html',{'select':select,'page':page,'number':number,})
    except:
        return HttpResponse('页码不正确')
def login(request):
    return render(request,'login.html')
def loginlogic(request):
    username=request.POST.get('username')
    psw=request.POST.get('psw')
    check=TUser.objects.filter(username=username,pass_field=psw)
    if check:
        request.session["login"] = "ok"
        return redirect('baiapp:index')
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