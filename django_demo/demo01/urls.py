from django.urls import path

import demo01.views

urlpatterns = [
    path('home/', demo01.views.home)
]
