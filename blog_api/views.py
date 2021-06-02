from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.views import APIView
from blog.models import Post, Category
from .serializers import PostSerializer
from django.conf import settings
# from todo.settings import CACHE_TTL
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class PostListCreateView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        a = ""
        if cache.get('post_list'):
            print(cache.get('post_list'))
            print('cache--------')
            a = cache.get('post_list')
        else:
            print('database--------')
            a = Post.objects.all()
            cache.set('post_list', a)
        serializer = PostSerializer(a, many=True)
        return Response(serializer.data)


class PostRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        response_data = ""
        if cache.get(post_id):
            print('cache', post_id)
            response_data = cache.get(post_id)
        else:
            response_data = Post.objects.get(id=post_id)
            cache.set(post_id, response_data)
            print('db', post_id)
        serializer = self.get_serializer(response_data)
        return Response(serializer.data)
