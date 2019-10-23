from django.urls import path
# import and use views.py file to detail
# how the patterns actually work when we do go there
# from . import views
from mysite.views import *

# from inside this folder '.', import the views from mysite
from . import views

urlpatterns = [
    path('', views.index, name='filmstack'), #base level pattern for anything besides admin to appear as
    path('login/', views.login, name='login'),
    # path('user/', views.user),
    # path('adminmanage/', views.manage, name='manage'),
]
