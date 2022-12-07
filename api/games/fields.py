from rest_framework import serializers
from .models import *

# class GameListingField(serializers.RelatedField):
#     def to_internal_value(self, data):
#         game_obj, created = Game.objects.get_or_create(**data)
#         return album_obj
#     def to_representation(self, value):
#         return {
#             "name": value.name
#         }