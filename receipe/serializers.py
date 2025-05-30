from rest_framework import serializers 
from myapp.models  import Reecipe,Tag

class ReceipeSerualizer(serializers.ModelSerializer):
    class Meta:
        model = Reecipe
        fields = ['id' ,'title' , 'time_minutes', 'prices' , 'link']
        read_only_fields = ['id']
        
class RecepiDeatailsSerialzier(ReceipeSerualizer):
    class Meta(ReceipeSerualizer.Meta):
        fields = ReceipeSerualizer.Meta.fields + ['description']
        

class TagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tag
        fields = ['id' ,'name']
        read_only_fields = ['id']
        