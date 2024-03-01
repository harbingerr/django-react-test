from django.urls import path
from .views import PlayerView, homePage

urlpatterns = [
    path('', homePage),
    path('api/player', PlayerView.as_view())
]
