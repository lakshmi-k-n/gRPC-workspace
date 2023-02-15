"""workstation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from workstation_app.views import (SignUpAPI,
                                    LoginAPI,
                                    ProjectAPI,
                                    FolderAPI,
                                    FileAPI
                                    )
from rest_framework import routers


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = []
urlpatterns += [
    path('signup/',SignUpAPI.as_view(),name='signup'),
    path('login/',LoginAPI.as_view(),name='login'),
    path('project/',ProjectAPI.as_view(),name='create_project'),
    path('folder/',FolderAPI.as_view(),name='create_folder'),
    path('file/',FileAPI.as_view(),name='create_file'),
]

# router.register(r'signup', SignUpAPI.as_view())
# urlpatterns = router.urls
