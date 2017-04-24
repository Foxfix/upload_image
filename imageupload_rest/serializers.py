from rest_framework import serializers 
from imageupload.models import UploadeImage 

class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadeImage 
        fields = ('pk', 'image',)