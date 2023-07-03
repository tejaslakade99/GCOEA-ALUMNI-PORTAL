from django.urls import path
from Accounts.views import *
urlpatterns = [
#     path('login/', login_page, name="login"),
    path('role/', select_role, name="role"),
    path('register-admin/',register_admin, name="register-admin"),
    path('register-faculty/',register_admin, name="register-faculty"),
    path('register-alumni/',register_admin, name="register-alumni"),
    path('register-student/',register_admin, name="register-student"),
#     path('register/', register, name="register"),
#     path('activate/<email_token>', activate_email, name="activate_email"),
#
]