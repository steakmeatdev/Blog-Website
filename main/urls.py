from django.urls import path
from main.views import (
    home,
    sign_up,
    create_post,
    auth_logout
)

urlpatterns = [
    path("", home, name = "home"),
    path("home/", home, name = "home"),
    path("sign-up/", sign_up, name = "sign_up"),
    path("create-post/", create_post, name = "create_post"),
    path("logout/", auth_logout, name = "logout")
]