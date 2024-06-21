"""
URL configuration for app project.

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
from django.urls import path, include
from itens.views import ItensListView, NewItemView, DeleteItemView, UpdateItemView
from accounts.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('itens/', ItensListView.as_view(), name='ItensList'),
    path('new/', NewItemView.as_view(), name='NewItem'),
    path('delete_item/<int:pk>', DeleteItemView.as_view(), name='DeleteItem'),
    path('register/', register_view, name='Register'),
    path('login/', login_view, name='Login'),
    path('logout/', logout_view, name = 'Logout' ),
    path('update_item/<int:pk>', UpdateItemView.as_view(), name='EditItem'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
