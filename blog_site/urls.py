"""
URL configuration for blog_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from .views import home, register, login,logout
from blogs.views import single_blog, search
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blogs/', include("blogs.urls")),
    path('blogs/<slug:link>/', single_blog, name='single_blog'),    
    path('search/', search, name='search'),
    path('register/', register, name='register' ),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', include("dashboard.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
