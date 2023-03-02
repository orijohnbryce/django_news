from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('ynet', views.serve_ynet),
    path('home', views.home, name="home"),
    path('temp', views.temp, name="temp"),
    path('temp2', views.temp2, name="temp2"),
    path('signup', views.create_user, name="signup"),
    path('edit/<pk>', views.edit_post, name="edit"),
    path('delete/<pk>', views.delete_post, name="delete"),
    path('login', LoginView.as_view(), name="login"),
]