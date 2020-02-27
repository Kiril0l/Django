from django.conf.urls import url
from home.views import home, index

urlpatterns = [
    url(r"^index/", index, name="index"),
    url(r"^$", home, name="home"),
]