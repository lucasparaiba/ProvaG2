from rest_framework import routers, serializers, viewsets
from frequencia.models import *

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = '__all__'

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    #horarios = HorariosSerializer(many= True)
    class Meta:
        model = Eleitor
        fields = '__all__'

    def create(self, validated_data):
        eleitor = Eleitor.objects.create(**validated_data)
        return eleitor

class CandidatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidatos
        fields = '__all__'

    def create(self, validated_data):
        return Candidatos.objects.create(**validated_data)

class VagasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vagas
        fields = '__all__'

    def create(self, validated_data):
        return Vagas.objects.create(**validated_data)

class VotarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votar
        fields = '__all__'

    def create(self, validated_data):
        return Votar.objects.create(**validated_data)
