from rest_framework import viewsets
from api_json.models import SalasUF, Filme
from api_json.serializer import SalasUFSerializer, FilmeSerializer

class SalasUFViewSet(viewsets.ModelViewSet):
    queryset = SalasUF.objects.all()
    serializer_class = SalasUFSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer