# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 19-03-27
# Author Yo
# Email YoLoveLife@outlook.com
from rest_framework import serializers
from ..models import DEVELOPER

__all__ = [
    'DEVELOPERSerializer', 'DEVELOPERDeleteSerializer'
]


class DEVELOPERSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEVELOPER
        fields = (
            'id', 'uuid', 'name'
        )


class DEVELOPERDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DEVELOPER
        fields = (
            'id', 'uuid'
        )

    def update(self, instance, validated_data):
        instance.visible()
        return super(DEVELOPERDeleteSerializer, self).update(instance, validated_data)