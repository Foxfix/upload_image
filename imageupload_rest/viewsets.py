from rest_framework import viewsets 
from .serializers import UploadImageSerializer 
from imageupload.models import UploadeImage 


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadeImage.objects.all()
    serializer_class = UploadImageSerializer