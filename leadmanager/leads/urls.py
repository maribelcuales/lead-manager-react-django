from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads') # register router with endpoint 'api/leads' passing in LeadViewSet and name we call 'leads'
urlpatterns = router.urls # urls will give us the urls registered with the endpoint 'api/leads'