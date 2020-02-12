from django.conf.urls import url

from Pay import views

urlpatterns = [
    url(r'^onlinepay/', views.online_pay, name='index'),
    url(r'^payjin66/', views.pay_jin66, name='jin66'),
    url(r'^paysancai/', views.pay_sancai, name='sancai'),
    url(r'^payrenshenguo/', views.pay_renshenguo, name='renshenguo'),
    url(r'^payxingshendan/', views.pay_xingshendan, name='xingshendan'),
    url(r'^payjineng/', views.pay_jineng, name='jineng'),
    url(r'^controllerjin66/', views.controller_pay_jin66, name='cjin66'),
    url(r'^controllersancai/', views.controller_pay_sancai, name='csancai'),
    url(r'^controllerrenshenguo/', views.controller_pay_renshenguo, name='crenshenguo'),
    url(r'^controllerxingshendan/', views.controller_pay_xingshendan, name='cxingshendan'),
    url(r'^controllerjineng/', views.controller_pay_jineng, name='cjineng'),
    url(r'^getpaidinfo/', views.get_paidinfo, name='paidinfo'),

    url(r'^myattribute/', views.my_attribute, name='myattribute'),

]
