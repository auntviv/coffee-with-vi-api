"""View module for handling requests about tags"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from coffeeapi.models import Tag


class TagView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """update"""
            
        tag = Tag.objects.get(pk=pk)
        tag.label = request.data["label"]
        tag.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags
    """
    class Meta:
        model = Tag
        fields = ('id', 'label')
        depth = 2
        