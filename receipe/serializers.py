from rest_framework import serializers 
from myapp.models  import Reecipe

class ReceipeSerualizer(serializers.ModelSerializer):
    class Meta:
        model = Reecipe
        fields = ['id' ,'title' , 'time_minutes', 'prices' , 'link']
        read_only_fields = ['id']
        
class RecepiDeatailsSerialzier(ReceipeSerualizer):
    class Meta(ReceipeSerualizer.Meta):
        fields = ReceipeSerualizer.Meta.fields + ['description']
        
        
        
        