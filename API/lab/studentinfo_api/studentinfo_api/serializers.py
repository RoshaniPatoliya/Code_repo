from rest_framework import serializers
from .models import Student_info

class Student_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student_info
        fields = ['id','Name','Age','Course','College']