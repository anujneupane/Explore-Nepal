from django.contrib import admin
from django.urls import path
from enroll import views 

urlpatterns = [
    path('',views.Home.as_view(), name='Home' ),
]
