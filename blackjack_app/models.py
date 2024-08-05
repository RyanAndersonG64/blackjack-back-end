from django.db import models
from django.contrib.auth.models import User

class Card (models.Model):

  def __init__(self, value, suit, image):
        self.value = value
        self.suit = suit
        self.image = image


class Profile (models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.TextField()
  last_name = models.TextField()
  balance = models.IntegerField(default = 0)
  earnings = models.IntegerField(default = 0)
  deposited = models.IntegerField(default = 0)
  bet = models.IntegerField(default=0)
  hand = models.ManyToManyField(Card)

  def __str__(self):
    return self.user.username

values = {'2' : 2, '3': 3, '4': 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K': 10, 'A' : 11}
suits = ['clubs', 'diamonds', 'hearts', 'spades']

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def number_of_decks(self, request):
       for i in range(1, request.data['decks']):
          self.cards.append([Card(value, suit) for value in values for suit in suits])