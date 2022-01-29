from django.db.models import fields
from rest_framework import serializers
from .models import gpu, cpu, power, hard, MOTHERBOARD, fan, ram, keybordandmouse, etc

class gpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = gpu
        fields = '__all__'

class cpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'
        
class powerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = power
        fields = '__all__'
        
class hardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hard
        fields = '__all__'
        
class MOTHERBOARDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MOTHERBOARD
        fields = '__all__'
        
class fanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fan
        fields = '__all__'
        

class ramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ram
        fields = '__all__'
        
class keybordandmouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = keybordandmouse
        fields = '__all__'
class etcSerializer(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = etc
        fields = '__all__'