from rest_framework import serializers
from api_json.models import SalasUF, Filme

class SalasUFSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalasUF
        fields = ['uf', 'qtd_salas', 'ano_atualizacao']

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['ano_lancamento', 'titulo', 'direcao', 'genero', 'empresa_produtora_br_majoritaria', 'uf', 'distribuidora', 'renda']
