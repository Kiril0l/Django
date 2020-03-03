from django.urls import path
from home.views import home, portfolio, about, contact

urlpatterns = [
    path("portfolio.html", portfolio, name="portfolio"),
    path("about.html", about, name="about"),
    path("contact.html", contact, name="contact"),
    path("index.html", home, name="home"),
]

