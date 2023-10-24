from rest_framework import routers
from .views import UserViewSet, UserCreateView

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls