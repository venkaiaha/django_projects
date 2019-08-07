
from django.urls import path
from django.conf.urls import url
from .rest_services import api_all_student,api_all_subject,api_hsc,api_lsc,api_avg,api_hpp,api_lpp,api_hsc,api_bsm

urlpatterns=[
    path('students/',api_all_student),
    path('subjects/',api_all_subject),
    path('2/',api_hsc),
    path('3/',api_lsc),
    path('4/',api_avg),
    path('5/',api_hpp),
    path('6/',api_lpp),
    path('7/',api_hsc),
    path('8/',api_bsm)
]