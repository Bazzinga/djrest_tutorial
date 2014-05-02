# -*- coding: utf-8 -*-

from django.forms import widgets

from rest_framework import serializers

from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()    # Note: 'Field' is an untyped read-only field

    title = serializers.CharField(max_length=100, required=False)

    # Notice that we can also use various attributes that would typically
    # be used on form fields, such as widget=widgets.Textarea.
    # These can be used to control how the serializer should render
    # when displayed as an HTML form. This is particularly useful
    # for controlling how the browsable API should be displayed.
    code = serializers.CharField(widget=widgets.Textarea,
                                 max_length=100000)

    linenos = serializers.BooleanField(required=False)

    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
                                       default='python')

    styles = serializers.ChoiceField(choices=STYLE_CHOICES,
                                    default='friendly')

    def restore_object(self, attrs, instance=None):
        """
        Create or update  a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """

        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.styles = attrs.get('styles', instance.style)
            return intance

        # Create new instance
        return Snippets(**attrs)
