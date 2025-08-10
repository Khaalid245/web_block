# blog/views/article_views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from blog.models.article import Article
from blog.serializers.article_serializer import ArticleSerializer

# Homepage view
def home(request):
    return HttpResponse("Welcome to the Blog Homepage!")

# API Views
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
