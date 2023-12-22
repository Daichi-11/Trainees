from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.user_signup, name='signup'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
]