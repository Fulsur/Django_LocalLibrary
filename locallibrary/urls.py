"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),      # 它将所有以catalog/开头的URL请求转发到catalog应用中的urls.py文件进行处理
    path('', RedirectView.as_view(url='/catalog/')),  # 将根URL重定向到/catalog/
    path('accounts/', include('django.contrib.auth.urls')),  # 包含Django内置的身份验证URL
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # 用于在开发环境中提供对静态文件的访问

