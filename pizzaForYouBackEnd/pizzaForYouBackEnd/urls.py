from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponseForbidden
from .views import OtherViews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/users/', include('users.urls')),
    path('get-csrf-token/', OtherViews.as_view(), name='csrf-token')
]

if not settings.DEBUG:
    urlpatterns[0] = path('admin/', lambda request: 
                          HttpResponseForbidden(f"""Forbidden: admin access disabled in production!: 
                                                {settings.DEBUG}"""))