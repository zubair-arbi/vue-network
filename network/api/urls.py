# -*- coding: utf-8 -*-
"""
URL definitions for Network API endpoint.
"""

from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url


urlpatterns = [
    url(
        r'^v1/',
        include('network.api.v1.urls', namespace='v1'),
        name='network_api_v1'
    ),
]
