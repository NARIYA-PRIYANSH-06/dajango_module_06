from rest_framework import serializers
from .models import *


class AuthorSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '_all_'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '_all_'
        # depth = 1

    def to_representation(self, instance):
        resp =  super().to_representation(instance)
        resp['author'] =AuthorSeralizer(instance.author).data
        return resp