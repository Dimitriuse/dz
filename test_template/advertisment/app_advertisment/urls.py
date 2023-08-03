from django.urls import path
from .views import index,top,login,profile,reg,add_post
urlpatterns = [
    path('add_post',add_post,name='add_post'),
    path('reg',reg,name='reg'),
    path('profile',profile,name='profile'),
    path('login',login,name='login'),
    path('',index,name='/'),
    path('top-sell',top,name='top'),
]
