# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render

from OrderFood.food.models import order,items


def home(request):
    context = {'dishes': order.objects.all()}
    o = order()
    o = context.get('dishes')
    for i in o:
        print(i.name)
    return render(request, "home.html", context)


def cart(request):
    val = request.GET.getlist('foodorder',default=None)
    # print(val)
    context = {'dishes': order.objects.all()}
    o = order()
    total = 0
    l = []
    o = context.get('dishes')
    for i in o:
        # print(i.name)
        for j in val:
            j = j.replace('/','')
            # print(j)
            if i.name == j:
                l.append(i)
                total += i.price
                # print(total)
    # fetch a result based on the name of the food name mentioned in result by using database
    context = {'Orderlist':l, 'bill':total}
    return render(request, 'result.html', context)


def confirmOrder(request):
    amt = request.GET['t']
    item = items()
    item.ord_id = random.randint(9999999,999999999)
    item.ord_price = amt
    item.ord_address = request.POST['address']
    item.save();
    return render(request, 'confirm.html')

def index(request):
    return render(request, 'index.html')

