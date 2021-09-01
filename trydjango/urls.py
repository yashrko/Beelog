"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from trydjango.settings import DEBUG
from django.contrib import admin
from django.urls import path,include
from users.views import signup_view,UserDetailView,UserUpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("blog.urls")),
    path('signup/',signup_view,name="signup-view"),
    path('login/',LoginView.as_view(template_name="login.html"),name="login-view"),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name="logout-view"),
    path('user/<int:pk>/',UserDetailView.as_view(template_name="userdetail.html"),name="user-detail-view"),
    path('user/<int:id>/update/',UserUpdateView,name="user-update-view")
]
if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
