from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('city/<int:pk>', views.CityDetail.as_view() ,name='CityDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)