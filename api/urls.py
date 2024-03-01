from django.urls import path
from .views import PlayerGetView, PlayerPostView, homePage

urlpatterns = [
    path('', homePage),
    path('api/player/get', PlayerGetView.as_view()),
    path('api/player/post', PlayerPostView.as_view()),
]
