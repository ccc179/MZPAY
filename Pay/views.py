# import json
import os
import time
import hashlib
from KEYS.keys import SECRET_KEYS
from OnlinePay.settings import BASE_DIR

from django.http import HttpResponse
from django.shortcuts import render
import paramiko

from Pay.models import OrderList
from Pay.tasks import take_item


def online_pay(request):
    context = {
        "title": "天道酬勤玩家自助中心"
    }
    return render(request, 'mz.html', context=context)


# 金柳露
def pay_jin66(request):
    context = {
        "title": "金柳露礼包"
    }
    return render(request, 'pay_jin66.html', context=context)


def controller_pay_jin66(request):
    extdata = request.POST.get('extdata')
    print(extdata)
    if extdata == "110":
        paymoney = 10  # 10
    elif extdata == "111":
        paymoney = 20  # 20
    elif extdata == "112":
        paymoney = 50  # 50
    context = {
        "gameuser": request.POST.get('gameuser'),
        "paymoney": paymoney,
        "extdata": extdata,
    }
    return render(request, 'jump.html', context=context)


# 三才勾玉
def pay_sancai(request):
    context = {
        "title": "三才勾玉礼包"
    }
    return render(request, 'pay_sancai.html', context=context)


def controller_pay_sancai(request):
    extdata = request.POST.get('extdata')
    if extdata == "113":
        paymoney = 58  # 58
    context = {
        "gameuser": request.POST.get('gameuser'),
        "paymoney": paymoney,
        "extdata": extdata,
    }
    return render(request, 'jump.html', context=context)


# 人参果
def pay_renshenguo(request):
    context = {
        "title": "人参果礼包"
    }
    return render(request, 'pay_renshenguo.html', context=context)


def controller_pay_renshenguo(request):
    extdata = request.POST.get('extdata')
    print(extdata)
    if extdata == "114":
        paymoney = 10  # 10
    context = {
        "gameuser": request.POST.get('gameuser'),
        "paymoney": paymoney,
        "extdata": extdata,
    }
    return render(request, 'jump.html', context=context)


# 醒神丹

def pay_xingshendan(request):
    context = {
        "title": "醒神丹礼包"
    }
    return render(request, 'pay_xingshendan.html', context=context)


def controller_pay_xingshendan(request):
    extdata = request.POST.get('extdata')
    if extdata == "115":
        paymoney = 10  # 10
    context = {
        "gameuser": request.POST.get('gameuser'),
        "paymoney": paymoney,
        "extdata": extdata,
    }
    return render(request, 'jump.html', context=context)


# 顶级技能自选包

def pay_jineng(request):
    context = {
        "title": "顶级技能自选包"
    }
    return render(request, 'pay_jineng.html', context=context)


def controller_pay_jineng(request):
    extdata = request.POST.get('extdata')
    if extdata == "116":
        paymoney = 20  # 20
    elif extdata == "117":
        paymoney = 50  # 50
    context = {
        "gameuser": request.POST.get('gameuser'),
        "paymoney": paymoney,
        "extdata": extdata,
    }
    return render(request, 'jump.html', context=context)


# 订单回执接口
def get_paidinfo(request):
    result = {
        'ordernumber': request.GET.get('ordernumber'),
        'userid': request.GET.get('userid'),
        'realmoney': request.GET.get('realmoney'),
        'gamecurrency': request.GET.get('gamecurrency'),
        'extdata': request.GET.get('extdata'),
        'sign': request.GET.get('sign')}
    print("验证秘钥")
    print(result)
    str_miyao = SECRET_KEYS + result.get('ordernumber')
    print(str_miyao)
    key1 = hashlib.md5(str_miyao.encode(encoding='utf-8')).hexdigest()
    print(key1)
    if result.get('sign') == key1:
        # 订单验证码对了就创建数据库信息，默认success是0，防止重复发放
        OrderList.objects.get_or_create(order_info=result)
        result_id = take_item.delay(result)
        print(result_id)
        return HttpResponse("ok")
    else:
        return HttpResponse("验证失败！")


def my_attribute(request):
    if request.method == 'GET':
        zhuan_list= [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0],
                       [6, 0], [7, 0], [8, 0], [9, 0]]
        return render(request, 'My_attribute.html', context=locals())
    elif request.method == 'POST':
        print("这里是post了")
        print(request.POST)
        level = int(request.POST.get('level_now'))
        result = (level - 1) * 5
        zhuan_1 = int(request.POST.get('zhuan_1'))
        if zhuan_1:
            result += (zhuan_1 - 50) * 5 + 2000
        zhuan_2 = int(request.POST.get('zhuan_2'))
        if zhuan_2:
            result += (zhuan_2 - 50) * 5 + 2000
        zhuan_3 = int(request.POST.get('zhuan_3'))
        if zhuan_3:
            result += (zhuan_3 - 50) * 5 + 2000
        zhuan_4 = int(request.POST.get('zhuan_4'))
        if zhuan_4:
            result += (zhuan_4 - 50) * 5 + 2000
        zhuan_5 = int(request.POST.get('zhuan_5'))
        if zhuan_5:
            result += (zhuan_5 - 50) * 5 + 2000
        zhuan_6 = int(request.POST.get('zhuan_6'))
        if zhuan_6:
            result += (zhuan_6 - 50) * 5 + 2000
        zhuan_7 = int(request.POST.get('zhuan_7'))
        if zhuan_7:
            result += (zhuan_7 - 50) * 5 + 2000
        zhuan_8 = int(request.POST.get('zhuan_8'))
        if zhuan_8:
            result += (zhuan_8 - 50) * 5 + 2000
        zhuan_9 = int(request.POST.get('zhuan_9'))
        if zhuan_9:
            result += (zhuan_9 - 50) * 5 + 2000

        print(result)
        return render(request, 'My_attribute.html',
                      context={'result': result, 'zhuan_list': [[1,zhuan_1], [2,zhuan_2], [3,zhuan_3], [4,zhuan_4], [5,zhuan_5],
                                                                [6,zhuan_6], [7,zhuan_7], [8,zhuan_8], [9,zhuan_9]],
                               'level_now':level})
