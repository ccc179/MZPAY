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
        "title": "吾爱梦猪"
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
        paymoney = 1  # 10
    elif extdata == "111":
        paymoney = 1  # 20
    elif extdata == "112":
        paymoney = 1  # 50
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
        paymoney = 1  # 58
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
        paymoney = 1  # 10
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
        paymoney = 1  # 10
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
        paymoney = 1  # 20
    elif extdata == "117":
        paymoney = 1  # 50
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
        'userid': request.GET.get('username'),
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
