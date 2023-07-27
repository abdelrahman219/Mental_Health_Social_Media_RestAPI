from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from .models import Comment, Post
from .serializers import CommentSerializer, PostSerializer
from .permissions import IsDoctorUser, IsOwnerOrReadOnly, IsCommentOwnerOrReadOnly

class CommentListCreateView(generics.ListCreateAPIView):
    # queryset = Comment.objects.filter(parent=None)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCommentOwnerOrReadOnly]


class Posts_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated , IsOwnerOrReadOnly]


class Posts_Pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer


class PostsByCreatorList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        creator_id = self.kwargs['creator_id'] 
        return Post.objects.filter(creator_id=creator_id)
