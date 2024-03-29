from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import PlayerSerializer
from .models import Player

# Create your views here.
class PlayerGetView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerPostView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

def homePage(request):
    return HttpResponse('HOME!')


