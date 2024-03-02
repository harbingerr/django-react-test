from django.urls import path
from .views import PlayerGetView, PlayerPostView, homePage

urlpatterns = [
    path('player/get', PlayerGetView.as_view()),
    path('player/post', PlayerPostView.as_view()),
]
