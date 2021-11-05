
from .models import Videogames
from rest_framework import viewsets, permissions
from .serializers import VideogameSerializer
# Create your views here.
class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogames.objects.all()
    serializer_class = VideogameSerializer
    permission_classes = [permissions.AllowAny]
