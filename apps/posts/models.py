from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    description = models.CharField(max_length=1000, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.email}, {self.pk}"
    
class PostFile(models.Model):
    def photo_upload(instance, filename):
        return f'post_files/{instance.user.email}/{instance.pk}'

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to = photo_upload)

    
