
from django.urls import path
from .views import post_index, post_detail, post_create, post_edit, post_delete

app_name = 'community'

urlpatterns = [
    path('', post_index, name='index'),
    path('post/<int:pk>/', post_detail, name='detail'),
    path('post/new/', post_create, name='create'),
    path('post/<int:pk>/edit/', post_edit, name='edit'),
    path('post/<int:pk>/delete/', post_delete, name='delete'),
]
