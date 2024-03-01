from django.urls import path
from .views import PlayerView, PlayerPostView, homePage

urlpatterns = [
    path('', homePage),
    path('api/player/get', PlayerView.as_view()),
    path('api/player/post', PlayerPostView.as_view()),
]
