from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutUser, name='logout'),
]
