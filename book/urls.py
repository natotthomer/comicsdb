from django.conf.urls import url
from django.contrib import admin

import book.views as views

urlpatterns = [
    url(r'^read/', views.read),
]
