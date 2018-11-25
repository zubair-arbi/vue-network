# -*- coding: utf-8 -*-
"""
URL definitions for version 1 of the Network API.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework.routers import DefaultRouter

from network.api.v1.views import AreaViewset, SystemViewset


router = DefaultRouter()
router.register('areas', AreaViewset, 'areas',)
router.register('systems', SystemViewset, 'systems',)

urlpatterns = []
urlpatterns += router.urls
