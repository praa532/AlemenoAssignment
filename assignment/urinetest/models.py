from django.db import models

# Create your models here.

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    # upload_datetime = models.DateTimeField(auto_now_add=True)

    def analyze_rgb(self):
        image_path = self.image.path
        return self.upload_image(image_path)

    def __str__(self):
        return self.image.name