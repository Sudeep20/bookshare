from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'sell'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^post_new/$',views.post_new,name='post_new'),
]
