from django.contrib import admin
from django.urls import path
from .views import blog_list_view, blog_detail_view

urlpatterns = [
    path('', blog_list_view, name='bloglistlink'),
    path('<int:id>/', blog_detail_view, name='bloglink'),
]






