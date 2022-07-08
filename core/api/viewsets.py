from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'enderecos__linha1']
    #permission_classes = [DjangoModelPermissions]
    authentication_classes = (TokenAuthentication,)



    '''Formas de filtragem'''

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    """
    Relativo ao método GET
    """

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    """
    Relativo ao método POST
    """

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    """
    Relativo ao método DELETE
    """

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    """
    Relativo ao método GET
    """
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    """
    Relativo ao método PUT
    """
    def partial_update(self, request, *args, **kwargs):
         return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    """
    Relativo ao método PATCH
    """

    @action(methods=['get'], detail=True)
    def denunciar (self, request, pk=None):
        pass

    """
    Relativo a uma ação em um recurso do endpoint, ou seja, um único objeto. Ex: .../pontoturistico/1/
    """

    @action(methods=['post'], detail=False)
    def teste (self, request):
        pass
    """
    Relativo a uma ação no endpointo como todo endpoint. Ex: .../pontoturistico/teste/
    """
