from django.contrib import admin
from django.urls import path
from main.views import access_request_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', access_request_view, name='access_request'),
]
