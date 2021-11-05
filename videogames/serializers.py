from .models import Videogames
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class VideogameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videogames
        fields = ['id', 'title', 'genre', 'publisher','developer','synopsis', 'image', 'video', 'trailer']