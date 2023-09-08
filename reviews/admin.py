from django.contrib import admin
from .models import Game, Publisher, GameReview, Genre

admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(GameReview)
admin.site.register(Genre)