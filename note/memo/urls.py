from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^postgres/$', views.postgres, name='postgres'),
    url(r'^$', views.memo_list, name='memo_list'),
    url(r'^new$', views.memo_create, name='memo_new'),
    url(r'^edit/(?P<pk>\d+)$', views.memo_update, name='memo_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.memo_delete, name='memo_delete'),
]