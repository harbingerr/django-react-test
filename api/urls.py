from django.urls import path
from .views import PlayerView, HomePage

urlpatterns = [
    path('', HomePage),
    path('api/player', PlayerView.as_view())
]
