from django.contrib import admin
from django.urls import path
from main import views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('admin-page',views.adminPage),
]