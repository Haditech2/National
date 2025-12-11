from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'members'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('id-card/', views.generate_id_card, name='generate_id_card'),
    path('id-card/preview/', views.IDCardPreviewView.as_view(), name='id_card_preview'),
    path('verify/<str:membership_id>/', views.VerifyMemberView.as_view(), name='verify_member'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='members/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='members/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='members/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='members/password_reset_complete.html'), name='password_reset_complete'),
]
