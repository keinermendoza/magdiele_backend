from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import (
    
    PostSerializer, 
    ComentSerializerGet, 
    ComentSerializerPost, 
    MensajeSerializer,
    ListPostSerializer
) 

from .models import Post, Comment, Mensaje

# GET
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPostSerializer
    # permission_classes = [permissions.AllowAny]

class LatestPost(generics.ListAPIView):

    queryset = Post.latest.all()[:3]
    serializer_class = ListPostSerializer
    # permission_classes = [permissions.AllowAny]
    
# GET
class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'
    queryset = Post.objects.all()

    # lookup_url_kwarg = 'slug'

    # def get_queryset(self):
    #     slug = self.kwargs.get('slug')
    #     return Post.objects.get(slug=slug)

# GET
class CommentList(generics.ListAPIView):
    serializer_class = ComentSerializerGet
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        comments = Comment.objects.filter(slug=slug)
        return comments
# POST  
class MensajeCreate(generics.CreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer

# POST
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ComentSerializerPost

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        user = self.request.user
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Post.NotFound("El post no existe")

        serializer.context['post'] = post
        serializer.context['user'] = user
        serializer.save()

# GET / UPDATE / DELETE
class CommentRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = ComentSerializerPost
    # permission_classes = [permissions.AllowAny]