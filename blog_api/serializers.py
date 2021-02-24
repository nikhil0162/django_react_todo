from rest_framework import serializers
from blog.models import (Post,
                         Category
                         )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'excerpt', 'content',
                  'author', 'status', )
