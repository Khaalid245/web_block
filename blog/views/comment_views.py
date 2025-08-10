from rest_framework import generics
from blog.models.comment import Comment
from blog.serializers.article_serializer import CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
