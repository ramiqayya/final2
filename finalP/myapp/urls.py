from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("admin", admin.site.urls),
    path("trade", views.trade, name="trade"),

    path("<str:name>", views.greet, name="swade"),


]
