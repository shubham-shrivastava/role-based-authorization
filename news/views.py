from django.shortcuts import render
from news.models import Article
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User, Group
from news.serializers import ArticleSerializer, UserSerializer
from rest_framework import permissions
from news.permissions import IsAdmin, CanChangeArticle
from django.contrib.auth.hashers import make_password
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (
        IsAdmin,
        )
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)
 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (
        IsAdmin,
        )
    
    def perform_update(self, serializer):
        if 'password' in self.request.data:
            password = make_password(self.request.data['password'])                                 
            serializer.save(password=password)                                                      
        else:
            serializer.save()

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CanChangeArticle,
        )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    name = 'article-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CanChangeArticle,
        )

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'articles': reverse(ArticleList.name, request=request),
            'users': reverse(UserList.name, request=request),
            })