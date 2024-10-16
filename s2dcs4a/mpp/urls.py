from django.urls import path
from . import views



urlpatterns =[
    path("",views.index, name = "index"),
    path("mymentor",views.mymentor, name = "mymentor"), #utk routing cth :  klklklk/ (ni)
    path('mystudent', views.mystudent, name='mystudent'),
    #path('hobby',views.hobby,name = 'hobby'),
    #path('update/<str:menid>',views.updatedate,name='updatedate'),
    #path('delete/<str:menid>',views.delete, name = 'delete'),
    path('viewdelete/<str:menid>',views.viewdelete, name = 'viewdelete'),
    #path('viewdelete/delete/<str:menid>',views.delete, name = 'delete'),
    ]