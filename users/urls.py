from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register),
    path('register/', views.RegisterAPIView.as_view()),
    # path('confirm/', views.confirm),
    path('confirm/', views.ConfirmAPIView.as_view()),
    # path('login/', views.login_view),
    path('login/', views.LoginAPIView.as_view()),
]