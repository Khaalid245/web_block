from rest_framework import serializers
from blog.models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'article', 'name', 'message', 'created_at']
