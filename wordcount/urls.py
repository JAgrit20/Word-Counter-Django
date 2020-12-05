
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('countthewords/',views.count,name='count'),
    path('admin/', admin.site.urls),
]
