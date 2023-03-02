from django.urls import path

from . import views_api

urlpatterns = [
    path('posts', views_api.serve_posts),
]