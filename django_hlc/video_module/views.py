from rest_framework import generics, permissions
from video_module import serializer
from video_module.models import Video

class VideoListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Video.objects.all()
    serializer_class = serializer.VideoSerializer
    
