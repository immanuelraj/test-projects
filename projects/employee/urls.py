from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('employee/', ListSongsView.as_view(), name="employees-all")
]