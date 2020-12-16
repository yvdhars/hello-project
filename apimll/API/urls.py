from django.urls import path, include
from.views import wineview
urlpatterns = [
    path('', wineview),
]