from django.urls import path
from Accounts.views import *
urlpatterns = [
    path('role/', select_role, name="role"),
    path('register/<slug:my_role>', register_admin, name="register-admin"),
    path('login/', login_page, name="login"),
    path('index/', index, name="index"),
    path('contact/', contact_us, name="contact us")
]