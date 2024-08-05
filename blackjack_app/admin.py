from django.contrib import admin

from blackjack_app.models import *

class ProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)

