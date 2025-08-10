from django.urls import path
from blog.views import ArticleListCreateView, ArticleDetailView, CommentCreateView, home

urlpatterns = [
    path('', home, name='home'),  # Optional homepage
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
]
