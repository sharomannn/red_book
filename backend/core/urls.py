from django.urls import path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from core import views

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/swagger/')),
    path('auth/', views.Auth.as_view(), name='auth'),
]

router = DefaultRouter()

router.register('users', views.User, basename='users')

urlpatterns += router.urls
