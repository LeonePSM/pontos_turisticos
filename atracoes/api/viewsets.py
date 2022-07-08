from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracoesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('nome', 'descricao')
