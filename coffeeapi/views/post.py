"""View module for handling requests about post types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from coffeeapi.models import Post



class PostView(ViewSet):
    """Post  view"""
    
    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def update(self, request, pk):
        """Handle PUT requests for a post
        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        serializer = CreatePostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def list(self, request):
       
        posts = Post.objects.filter(user=request.auth.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # add this line at the top with the other imports

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized post instance
        """
        
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.auth.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'imageUrl', 'tags', 'datetime')
        depth = 2
    #user should be added to fields if you plan on using it 
    #depth recognizes nested data
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id','title', 'description', 'imageUrl', 'tags', 'datetime' ]
       
        
    #new serializer that will include fields that are expected from the client