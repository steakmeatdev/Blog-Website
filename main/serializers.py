from rest_framework import serializers
from .models import model_

class model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = model_
        fields = ['title', 'description']

    # I can ovverdie validate() method