from django.conf.urls import url

from OrderFood.food.views import home, cart, confirmOrder, signup, register, now_login, dologin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'cart', cart, name='cart'),
    url(r'dologin', dologin, name='dologin'),
    url(r'register', register, name='register'),
    url(r'confirm', confirmOrder, name='confirm'),
    url(r'cancel', home, name='cancel'),
    url(r'signup', signup, name='signup'),
    url(r'now_login', now_login, name='now_login')
]