
from django.urls import path
from authorityapp import views

urlpatterns = [
    path('',views.Home,name="Home")

]