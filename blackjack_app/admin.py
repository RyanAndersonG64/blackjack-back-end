from django.contrib import admin

from blackjack_app.models import *

class ProfileAdmin(admin.ModelAdmin):
  pass

class ImageAdmin(admin.ModelAdmin):
  pass

class CardAdmin(admin.ModelAdmin):
  pass

class DeckAdmin(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)

