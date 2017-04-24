import uuid
from django.db import models

def scramble_uploaded_filename(instance, filename):
    extension = filename.split('.')[-1]
    return '{}.{}'.format(uuid.uuid4(), extension)

class UploadeImage(models.Model):
    image = models.ImageField('Uploade image', upload_to=scramble_uploaded_filename)
