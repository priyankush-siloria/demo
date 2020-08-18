from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    # URL's same for both role
    path('search', SearchData.as_view()),

]