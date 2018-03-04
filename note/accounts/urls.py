from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .views import register_view, login_view, logout_view

urlpatterns = [
    # url(r'^$', views.signin),
    url(r'^join/$', register_view, name='join'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'), #로그아웃 후 홈으로 이동
]