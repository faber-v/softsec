from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.UserLogin, name='login'),
    url(r'^logout/$', views.UserLogout, name='logout'),
    url(r'^orders/$', views.ListOrders, name='orders'),
]
