from rest_framework import serializers
from .models import Post

from authentication.serializers import AccountSerializer
from authentication.models import Account



class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all(), write_only=True)
    category = serializers.CharField(source='get_category_display')
    class Meta:
        model = Post
        fields = ['author', 'author_id', 'created_at', 'updated_at', 'img', 'name', 'area', 'address', 'dish', 'category', 'expense', 'note', 'rating']
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['author'] = validated_data.get('author_id', None)

        if validated_data['author'] is None:
            raise serializers.ValidationError("author not found.") 

        del validated_data['author_id']

        return Post.objects.create(**validated_data)
