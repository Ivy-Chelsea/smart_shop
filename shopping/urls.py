from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('category/<str:name>',views.products,name='producs'),
    path('order/<str:name>',views.order,name='order'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('buy/<str:name>',views.buy,name='buy'),
    path('myorder',views.myorder,name='myorder'),
    
]