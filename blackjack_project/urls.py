from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from blackjack_app.views import *
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from blackjack_app.views import *

router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('get-profile/', get_profile),
    path('create-user/', create_user),
    path('decks/', DeckViewSet.as_view({'get': 'list'})),
    path('get-decks/', get_decks),
]
