from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='equipment/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='equipment/logout.html'), name='logout'),
    path('lists/', views.list_view, name='list_view'),
    path('add_item/', views.add_item, name='add_item'),
    path('create_list/', views.create_list, name='create_list'),
    path('lists/<int:pk>/', views.list_details, name='list_details'),
    path('lists/<int:pk>/share/', views.share_list, name='share_list'),
]
