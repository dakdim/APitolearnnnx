from rest_framework import serializers
from .models import Moviedata

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model=Moviedata
        fields=['id','name','duration','rating']