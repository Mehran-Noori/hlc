from video_module import models
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = "__all__"