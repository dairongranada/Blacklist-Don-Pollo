"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from blacklist.api import urls
from config import settings
from blacklist import views
admin.site.site_header = 'BLACKLIST'
admin.site.index_title = 'VISTA ADMINISTRADOR'
admin.site.site_title = 'BLACKLIST'

urlpatterns = [
    # path('jet/', include('jet.urls','jet')),  # Django JET URLS

    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include('blacklist.api.urls')),
    path('web/', include('blacklist.urls')),
    path('', include('django.contrib.auth.urls')), #autenticacion por sesion
    path('', views.home, name='home'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
