from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from helptutor.services.api import *

router = DefaultRouter()
router.register('service', ServiceAPIView)
router.register('offer', OfferAPIView)
# router.register('contract', ContractViewSet)
# router.register('aggrement', AggrementViewSet)
# router.register('nomination', NominationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
