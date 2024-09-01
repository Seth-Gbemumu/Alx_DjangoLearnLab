from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Modelserializer):
    class Meta:
        model = Book
        fields = ['titles', 'author']
