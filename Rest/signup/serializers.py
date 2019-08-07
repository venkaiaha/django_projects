from .models import SignUp
from rest_framework import serializers
class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=SignUp
        fields=('id','name','password')