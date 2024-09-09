import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blackjack_project.settings')  # Adjust this to your project settings path
django.setup()

from blackjack_app.models import Card, Deck

# def populate_decks():
#     values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
#     suits = ['clubs', 'diamonds', 'hearts', 'spades']

#     cards = []
#     for value in values:
#         for suit in suits:
#             card = Card.objects.create(value=value, suit=suit)
#             cards.append(card)

#     for _ in range(6):
#         deck = Deck.objects.create()
#         deck.cards.set(cards)
#         deck.save()

# populate_decks()