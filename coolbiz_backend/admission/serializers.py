from rest_framework import serializers
from .models import Admission

class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ('id', 'username', 'first_name', 'last_name',)
        #read_only_fields = ('username', )
