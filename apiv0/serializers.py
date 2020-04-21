from rest_framework import serializers
from .models import Post

from authentication.models import Account



class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=Account.objects.all())
    class Meta:
        model = Post
        fields = ['id', 'author', 'img', 'name', 'area', 'address', 'dish', 'category', 'expense', 'note', 'rating']


