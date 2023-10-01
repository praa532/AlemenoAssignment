from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer, save_rgb_as_json
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
            # Process and save RGB data as JSON
            image_instance = serializer.instance
            json_data = save_rgb_as_json(image_instance)  # Call your processing function
            
            if json_data is not None:
                serializer.instance.processed_data = json_data
                serializer.instance.save()
            
            # Render the response, you can replace "index.html" with your desired template
            return render(request, "index.html", serializer.data)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





