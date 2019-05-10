# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import LOCATION

__all__ = [
    'LOCATIONSerializer'
]


class LOCATIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOCATION
        fields = (
            'id', 'uuid', 'name'
        )


class LOCATIONDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LOCATION
        fields = (
            'id', 'uuid'
        )

    def update(self, instance, validated_data):
        instance.visible()
        return super(LOCATIONDeleteSerializer, self).update(instance, validated_data)