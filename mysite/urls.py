"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    #2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import post_list, post_detail, post_new, post_edit



urlpatterns = [

    #path('admin/', admin.site.urls),#admin ile başlayan her url için ona uyan bir view bulur.

    url(r'^admin/', admin.site.urls),

    url(r'^$', post_list),
    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
    #path('post/new', views.post_new, name='post_new'),
    url(r'^post/new/$', post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),

    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


    #url('post/<int:pk>/', post_detail, name='post_detail'),

    #url(r'^$/', include('blog.urls')), #django artık anasayfaya gelen herşeyi blog.urls e yönlendirecek ve oradaki yönergelere bakacak
]
