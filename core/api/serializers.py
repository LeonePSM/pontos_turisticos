from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    enderecos = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao',
                  'foto', 'enderecos', 'atracoes',
                  'avaliacoes', 'exemplo')
        read_only_fields =('comentarios', 'atracoes')


    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validate_data, validated_data=None):
        atracoes = validated_data['atracoes']
        del validate_data['atracoes']

        endereco = validate_data['enderecos']
        del validate_data['endereco']

        ponto = PontoTuristico.objects.create(**validate_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()

        return ponto