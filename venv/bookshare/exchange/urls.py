from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'exchange'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^exchange_new/$',views.exchange_new,name='exchange_new'),
    url(r'^home/$',views.home,name='home')
]
