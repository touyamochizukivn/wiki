from django.contrib import admin
from django.urls import path

from ts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ts', ts, name='ts')
]