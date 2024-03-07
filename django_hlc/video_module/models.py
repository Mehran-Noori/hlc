from django.db import models
from django.utils.text import slugify


class Video(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="video title", null=False, blank=False, required=True)
    slug = models.SlugField(_("video_slug"))
    file = models.FileField(upload_to="files/videos", null=False)
    created_at = models.DateTimeField(
        verbose_name='created at', auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(
        verbose_name='last update', auto_now=True, null=True)

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.url_title)
        super().save(*args, **kwargs)
