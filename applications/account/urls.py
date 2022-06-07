from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, LogOutView, ChangepasswordView, ForgotPasswordCompleteView, ForgotPasswordView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('change_password/', ChangepasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view()),
]