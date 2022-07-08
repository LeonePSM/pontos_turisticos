from rest_framework import viewsets
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.filter(aprovado=True)