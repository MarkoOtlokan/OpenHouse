from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from views import *

router = DefaultRouter()
router.register(r'House',HouseViewSet)
router.register(r'Rasperrypi',RasperrypiViewSet)
router.register(r'HouseNetwork',HouseNetworkViewSet)
router.register(r'TerminalRasperrypi',TerminalRasperrypiViewSet)
router.register(r'Inmate',InmateViewSet)
router.register(r'Function',FunctionViewSet)

urlpatterns = [
    url(
            r'^v1/',
                include(
                            router.urls,
                        ),
            ),
        ]