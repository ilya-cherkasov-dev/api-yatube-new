from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Посты: читать может любой авторизованный, менять только автор."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        # Автора беру из токена, а не из тела запроса.
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Группы доступны только для чтения, создаются через админку."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Комментарии к посту, id которого передан в адресе."""

    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)

    def get_post(self):
        # Если поста нет, сразу отдаю 404.
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
