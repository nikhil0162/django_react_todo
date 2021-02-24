from django.urls import path
from .views import PostRUDView, PostListCreateView

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostRUDView.as_view(), name='post-detail'),
    path('', PostListCreateView.as_view(), name='post-list')
]
