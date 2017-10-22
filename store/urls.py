from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^$', views.store, name='index'),
]
