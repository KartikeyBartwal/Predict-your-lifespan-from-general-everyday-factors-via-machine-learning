"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from app import views 

import logging
logger = logging.getLogger(__name__)

# ...

def LoginPage(request):
    logger.debug("LoginPage URL: %s   \n\n\n\n\n\n\n\n\n\n\n", request.build_absolute_uri())

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.SignupPage,name = "signup"),
    path('Signup/',views.SignupPage,name='signup'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/',views.HomePage,name="home"),
    path('home/outputPage',views.OutputPage,name="output_page"),
]
