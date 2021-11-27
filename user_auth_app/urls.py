from django.conf.urls import url
from user_auth_app import views
from django.urls import path

# TEMPLATE URLS
app_name= 'user_auth_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name="user_login"),
]
