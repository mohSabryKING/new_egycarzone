"""
URL configuration for new_carzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import *
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import *
from django.conf import settings
from .settings import *
urlpatterns = [
      
    #path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('',include('core.links')),
    path('',include('django.contrib.auth.urls')),
    
    #path('', include('admin_datta.urls')),
    #path('', include('admin_argon.urls')),
    
    #path('', include('admin_volt.urls')),
    
        #path('', include('admin_material.urls')),
    #path('', include('django_rocket.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)

#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler500="core.views.E500"
handler400="core.views.E400"
handler404="core.views.E404"
handler403="core.views.E403"
handler400="core.views.E400"
