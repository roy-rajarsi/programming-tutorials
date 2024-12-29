from django.urls import path
from .views import Hello


urlpatterns = [
    path(str(), Hello.as_view(), name='Hello')
]
