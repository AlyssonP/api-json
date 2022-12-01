from api_json.viewset import SalasUFViewSet, FilmeViewSet
from rest_framework import routers

router  = routers.DefaultRouter()
router.register("salasuf", SalasUFViewSet)
router.register("filmes", FilmeViewSet)