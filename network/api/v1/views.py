# -*- coding: utf-8 -*-
"""
A generic API for Network application.
"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from network.models import Area, System
from network.api.v1 import serializers


class AreaViewset(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer


class SystemViewset(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = System.objects.all()
    serializer_class = serializers.SystemSerializer
