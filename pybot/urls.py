from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('t1',views.t1,name='t1'),
    path('t2',views.t2,name='t2'),
   
    path('get/',views.get_bot_response,name='get_bot_response'),

    
]