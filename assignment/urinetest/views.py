from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer
import cv2
import numpy as np


# Create your views here.
def index(request):
    return render(request, "index.html")

@api_view(['POST'])
def upload_image(request):
    serializer = UploadedImageSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the image
        serializer.save()
        
        try:
            # Analyze RGB values
            image_instance = serializer.instance
            image_path = image_instance.image.path
            image = cv2.imread(image_path)
            rgb_values = np.mean(image, axis=(0, 1)).astype(int)
            
            # Add RGB data to the serializer
            serializer.data['rgb_data'] = {
                'average_rgb': rgb_values.tolist(),
            }
            
            # Render the response, you can replace "index.html" with your desired template
            return render(request, "index.html", serializer.data)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





