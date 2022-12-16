from django.contrib import admin
from django.urls import path

from apps.core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]