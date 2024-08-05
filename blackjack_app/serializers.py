from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = '__all__'

class DeckSerializer(serializers.ModelSerializer):
  class Meta:
    model = Deck
    fields = '__all__'
