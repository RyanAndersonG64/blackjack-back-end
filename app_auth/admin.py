from django.contrib import admin

from app_auth.models import *

class ProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)

