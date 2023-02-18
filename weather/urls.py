from django.urls import path, include

from weather.views import index
urlpatterns = [
    path("", index, name="index")
]