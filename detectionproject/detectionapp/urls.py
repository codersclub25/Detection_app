from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('detect',views.detect,name='detect'),
    path('camera',views.camera,name='camera')
]