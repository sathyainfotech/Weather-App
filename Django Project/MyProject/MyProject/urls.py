
from django.contrib import admin
from django.urls import path
from WeatherApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('delete/<CName>',views.delete_city,name="DCity")
]
