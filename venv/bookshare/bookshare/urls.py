"""bookshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from contact import views as contact_view
from profiles import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name="home"),
    url(r'^special/',contact_view.special,name='special'),
    url(r'^home/', include('profiles.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^sell/', include('sell.urls')),
    url(r'^exchange/', include('exchange.urls')),
    url(r'^advertisement/', include('advertisement.urls')),
    url(r'^logout/$', contact_view.user_logout, name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
