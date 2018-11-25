# -*- coding: utf-8 -*-
"""
A generic API for Network application.
"""
from rest_framework import viewsets

from network.models import Area, System
from network.api.v1 import serializers


class AreaViewset(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer


class SystemViewset(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = serializers.SystemSerializer
