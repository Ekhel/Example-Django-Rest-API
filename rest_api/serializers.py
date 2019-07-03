from rest_framework import serializers
from .models import Nelayan

class NelayanSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nelayan
        fields = ('id','nama','umur','distrik','kampung')
