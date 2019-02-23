"""carshopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from carshopapp import views

from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('carshop/sign-in/', LoginView.as_view(template_name='carshop/sign_in.html'),
        name='carshop-sign-in'),
    path('carshop/sign-out', LogoutView.as_view(next_page='/'),
        name='carshop-sign-out'),
    path('carshop/', views.carshop_home, name='carshop-home'),

    path('carshop/sign-up/', views.carshop_sign_up, name='carshop-sign-up'),

    path('carshop/account/', views.carshop_account, name='carshop-account'),
    path('carshop/car/', views.carshop_car, name='carshop-car'),
    path('carshop/car/add/', views.carshop_add_car, name='carshop-add-car'),
    path('carshop/car/edit/<int:car_id>', views.carshop_edit_car, name='carshop-edit-car'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
