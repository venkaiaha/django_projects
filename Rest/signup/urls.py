from django.urls import path
from .rest_services import api_all,api_add_new_user
urlpatterns=[
    path('all/',api_all),
    path('add/',api_add_new_user),
]