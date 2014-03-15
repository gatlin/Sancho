from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import PostSerializer, ContentTypeSerializer,\
        LinkSerializer
from sancho.models import Post, ContentType, Link
from rest_framework.permissions import IsAuthenticated, TokenHasReadWriteScope
from rest_any_permissions.permissions import AnyPermissions
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

class PostViewSet(viewsets.ModelViewSet):
    '''
    A viewset for orders
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [AnyPermissions]
    any_permission_classes = [IsAuthenticated, TokenHasReadWriteScope]

    def retrieve(self, request, pk=None):
        queryset = Post.objects.filter(uid=pk).all()

class ContentTypeViewSet(viewsets.ModelViewSet):
    '''
    A way to render all content types in the system
    '''
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    permission_classes = [AnyPermissions]
    any_permission_clasess = [IsAuthenticated, TokenHasReadWriteScope]

class LinkViewSet(viewsets.ModelViewSet):
    '''
    Links are relations among posts
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    permission_classes = [AnyPermissions]
    any_permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
