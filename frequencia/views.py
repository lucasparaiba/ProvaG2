from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from frequencia.models import *
from frequencia.serializers import *

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class CandidatosViewSet(viewsets.ModelViewSet):
    queryset = Candidatos.objects.all()
    serializer_class = CandidatosSerializer

class VagasViewSet(viewsets.ModelViewSet):
    queryset = Vagas.objects.all()
    serializer_class = VagasSerializer

class VotarViewSet(viewsets.ModelViewSet):
    queryset = Votar.objects.all()
    serializer_class = VotarSerializer
