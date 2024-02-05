"""
URL configuration for SiteToRssFeed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from authentication.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from user.viewsets import UserViewSet
from feed.views import get_html_code, get_search_pattern, preview
from feed.viewsets import FeedViewSet

router = routers.SimpleRouter()

# AUTHENTICATION
router.register(r'auth/login', LoginViewSet, basename="auth-login")
router.register(r'auth/register', RegistrationViewSet, basename="auth-register")
router.register(r'auth/refresh', RefreshViewSet, basename="auth-refresh")

# USER
router.register(r'user', UserViewSet, basename="user")

# FEED
router.register(r'feeds', FeedViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_html_code, name="index"),
    path("extract_pattern/", get_search_pattern, name="get_search_pattern"),
    path("preview/", preview, name="preview"),
]

urlpatterns += router.urls
