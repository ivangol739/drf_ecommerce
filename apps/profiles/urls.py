from django.urls import path

from apps.profiles.views import ProfileView

urlpatterns = [
    path("", ProfileView.as_view()),
]

