from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    enderecos = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'enderecos', 'atracoes', 'avaliacoes', 'exemplo')
