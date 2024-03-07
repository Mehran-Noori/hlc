from django.urls import path
from video_module import views
urlpatterns = [
    path('list', views.VideoListView.as_view())
    
]