# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.contrib.auth.models import User
from django.shortcuts import render

from OrderFood.food.models import order,items


def home(request):
    context = {'dishes': order.objects.all()}
    o = order()
    o = context.get('dishes')
    # for i in o:
    #     print(i.name)
    return render(request, "home.html", context)


def signup(request):
    if request == "GET":
        return render(request, "signup.html")
    else:
        uname = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']

        user = User.objects.create_user(username=fname, first_name=fname, last_name=lname, email = email, password = pwd)
        user.save();
        print("user saved")
        return render(request, "register.html")


def register(request):
    return render(request, "signup.html")


def dologin(request):
    print("request came for get!!")
    return render(request, "login.html")


def now_login(request):
    print("In post")
    if request == "POST":
        print("request came in post!!")
        u_name = request.POST.get['username']
        pwd = request.POST.get['password']

        context = {'users': User.objects.all()}
        user = User()
        user = context.get('users')

        print("request came!!")

        for u in user:
            print(u.username)

    #     for u in user:
    #         if u.username != u_name:
    #             msg = "user is not registered"
    #             return render(request, "signup.html", {'message': msg})
    #         else:
    #             if u.username == u_name:
    #                 if (pwd != u.password):
    #                     msg = "password incorrect"
    #                     return render(request, "login.html", {'message': msg})
    #                 else:
    #                     msg = "user logged in"
    #                     request.session['user'] = u
    #                     fav = request.session.get('user')
    #                     print(fav)
    #                     return render(request, "home.html", {'user': u})
    # else:

        return render(request, "home.html")



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

