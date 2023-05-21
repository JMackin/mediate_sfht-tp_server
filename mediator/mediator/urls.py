"""mediator URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('media', views.media_root),
    # TV
    path('media/tv/', views.tv_main),
    path('media/tv/<str:title>', views.tv_show),
    path('media/tv/<str:title>/<int:season>/', views.show_seasons),
    path('media/tv/<str:title>/<int:season>/<int:episode>', views.show_seasons),
    # Books
    path('media/books/', views.books_main),
    path('media/books<int:topic>/', views.books_by_topic),
    # Misc
    path('media/misc/', views.misc)

]
