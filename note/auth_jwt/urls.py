from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .views import UserLoginAPIView

urlpatterns = [
    # url(r'^$', views.signin),
    url(r'^join/$', views.signup, name='join'),
    # url(r'^login/$', views.signin, name='login'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}, name='logout'), #로그아웃 후 홈으로 이동
]