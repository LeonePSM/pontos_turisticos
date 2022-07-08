from rest_framework import viewsets
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        return Avaliacao.objects.filter(aprovado=True)