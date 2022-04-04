from django.urls import path

import word_counter.views

urlpatterns = [
    path('',word_counter.views.index , name="index"), #https://도메인
    path('result/',word_counter.views.result, name="result"), #https://도메인/result/
]
