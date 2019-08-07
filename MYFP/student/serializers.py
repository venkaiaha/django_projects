from .models import Student,Subject
from rest_framework import serializers
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=("subject","faculty")
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("sname","subject","marks")