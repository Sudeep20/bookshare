from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# SET THE NAMESPACE!
app_name = 'advertisement'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^home/$', views.home, name='home'),
    url(r'^uploads/form/$',views.model_form_upload,name='model_form_upload'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)