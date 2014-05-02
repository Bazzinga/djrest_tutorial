# -*- coding: utf-8 -*-

from django.forms import widgets

from rest_framework import serializers

from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ('id', 'title', 'code', 'linenos', 'language', 'styles')
