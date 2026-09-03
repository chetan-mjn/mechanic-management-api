from rest_framework.routers import DefaultRouter
from .views import MechanicViewSet

router = DefaultRouter()
router.register("mechanics", MechanicViewSet)

urlpatterns = router.urls