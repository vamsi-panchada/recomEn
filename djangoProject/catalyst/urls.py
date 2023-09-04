from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path('^/detail/(?P<id>[\w-]+)/$', views.detail, name='detail'),
    #path(r'^user/(?P<username>\w{0,50})/$', views.detail),
    path('detail/', views.detail),
    path('newoffer/', views.newoffer),
]