from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create_user/', views.RegisterView.as_view(), name='add_user')
]