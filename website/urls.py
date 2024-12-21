from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_page),
    path('index 1',index1_page),
    path('index 2',index2_page),
    path('index 2 light',index2light_page),
    path('index light',indexlight_page)
]
