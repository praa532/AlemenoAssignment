from rest_framework import serializers
from .models import UploadedImage
import json

class UploadedImageSerializer(serializers.ModelSerializer):
    processed_data = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = UploadedImage
        fields = '__all__'

def save_rgb_as_json(image):
    rgb_data = image.analyze_rgb()
    if 'error' in rgb_data:
        return None
    json_data = json.dumps(rgb_data)
    
    # Save the JSON data to a file or database field, depending on your needs.
    return json_data
