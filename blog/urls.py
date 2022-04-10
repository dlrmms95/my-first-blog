from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.post_list, name='post_list'),
    #url(r'^$', post_list),

    #url(r'^index/$', post_index),
    #url(r'^detail/$', post_detail),
    #url(r'^create/$', post_create),
    #url(r'^update/$', post_update),
    #url(r'^delete/$', post_delete),
]
