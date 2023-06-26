from django.urls import path
from Accounts.views import *
urlpatterns = [
#     path('login/', login_page, name="login"),
    path('role/', select_role, name="role"),
#     path('register/', register, name="register"),
#     path('activate/<email_token>', activate_email, name="activate_email"),
#
]