from django.conf.urls import url

from OrderFood.food.views import home, cart, confirmOrder

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'cart', cart, name='cart'),
    url(r'confirm', confirmOrder, name='confirm'),
    url(r'cancel', home, name='cancel')
]