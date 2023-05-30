from django.urls import path
from sitepages import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
