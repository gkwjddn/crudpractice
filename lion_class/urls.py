from django.contrib import admin
from django.urls import path, include
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name='home'),
    path('post/', include('blogapp.urls')),
]
