from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet

router = DefaultRouter()
router.register("service-requests", ServiceRequestViewSet)

urlpatterns = router.urls