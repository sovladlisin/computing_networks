from rest_framework import serializers
from backend.models import List, Person, System, Markup_Person, Markup_System


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'

class Markup_PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markup_Person
        fields = '__all__'

class Markup_SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markup_System
        fields = '__all__'