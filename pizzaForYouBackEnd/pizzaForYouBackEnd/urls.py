from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponseForbidden

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('users.urls')),
]

if not settings.DEBUG:
    urlpatterns[0] = path('admin/', lambda request: 
                          HttpResponseForbidden("Forbidden: admin access disabled in production!"))