from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from .models import Post
from .serializers import PostSerializer

class PostView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]
    search_fields = ['author__id']
