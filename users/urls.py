from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', LoginView.as_view()),
    path('token/refresh/', RefreshView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view()),
]
