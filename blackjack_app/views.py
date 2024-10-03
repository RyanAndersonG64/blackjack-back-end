
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

from .models import *
from .serializers import *

import random

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
  print('request', request)
  user = request.user
  profile = user.profile
  serialized_profile = ProfileSerializer(profile)
  return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
  user = User.objects.create(
    username = request.data['username'],
  )
  user.set_password(request.data['password'])
  user.save()
  profile = Profile.objects.create(
    user = user,
    first_name = request.data['first_name'],
    last_name = request.data['last_name']
  )
  profile.save()
  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = Image.objects.all()
   serializer_class = ImageSerializer
   
  #  def list(self, request):
  #       images = Image.objects.all()
  #       serializer = self.get_serializer(images, many=True)
  #       return Response(serializer.data)

class DeckViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    def list(self, request):
        num_decks = int(request.query_params.get('num_decks', 1))
        decks = Deck.objects.all()[:num_decks]
        serializer = self.get_serializer(decks, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_decks(request):

   cards = []
   decks = int(request.query_params.get('deck_number', 1))

   for i in range(decks):
      deck = Deck.objects.get(pk = 25) #pk needs to be updated if decks are remade
      cards.extend(deck.cards.all())

   random.shuffle(cards)

   cards_serialized = CardSerializer(cards, many = True)
   return Response(cards_serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
   images = Image.objects.all()
   images_serialized = ImageSerializer(images, many=True)
   return Response(images_serialized.data)