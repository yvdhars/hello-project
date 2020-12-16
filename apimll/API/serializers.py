from rest_framework import serializers
from .models import winequaity

class winequaityserializer(serializers.ModelSerializer):
    class Meta:
        model=winequaity
        fields=['fixedacidity', 'volatileacidity', 'citricacid', 'residualsugar', 'chlorides', 'freesulfurdioxide', 'totalsulfurdioxide', 'density','pH', 'sulphates', 'alcohol']