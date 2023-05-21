from django.urls import path
from .views import Home, Register, Login, Logout, Profile, Settings, UpdateEmail, UpdatePassword, ResetPasswordRequest, ResetPasswordRequestDone, ResetPassword, DeleteAccount

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    
    path('profile/<slug>/', Profile.as_view(), name='profile'),
    
    path('settings/', Settings.as_view(), name='settings'),
    path('settings/update-email/<slug>', UpdateEmail.as_view(), name='update-email'),
    path('settings/update-password/', UpdatePassword.as_view(), name='update-password'),

    path('reset-password-request/', ResetPasswordRequest.as_view(), name='reset-password-request'),
    path('reset-password-request/done/', ResetPasswordRequestDone.as_view(), name='reset-password-request-done'),
    path('reset-password/<uidb64>/<token>/', ResetPassword.as_view(), name='reset-password'),
    
    path('settings/delete-account/<slug>', DeleteAccount.as_view(), name='delete-account'),
]
