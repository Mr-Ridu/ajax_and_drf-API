from rest_framework import serializers
from .models import employee_information

class EmployeeSeriailizer(serializers.Serializer):
    em_name = serializers.CharField(max_length=50)
    em_email = serializers.EmailField()
    em_phn =  serializers.CharField(max_length=14) 

    #to create new object
    def create(self,validate_data):
        return employee_information.objects.create(**validate_data)
    
    #to update existing object
    def update(self, instance, validated_data):
        instance.em_name = validated_data.get('em_name',instance.em_name)
        instance.em_email = validated_data.get('em_email',instance.em_email)
        instance.em_phn = validated_data.get('em_phn',instance.em_phn)
        instance.save()
        return instance