from rest_framework import serializers
from authentication.serializers import AccountSerializer
from django.conf import settings
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['author'] = AccountSerializer(read_only=True)
        return super(PostSerializer, self).to_representation(instance)