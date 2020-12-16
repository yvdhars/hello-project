from django.db import models

# Create your models here.
class winequaity(models.Model):
    fixedacidity=models.FloatField(max_length=10)
    volatileacidity=models.FloatField(max_length=10)
    citricacid=models.FloatField(max_length=10)
    residualsugar=models.FloatField(max_length=10)
    chlorides=models.FloatField(max_length=10)
    freesulfurdioxide=models.FloatField(max_length=10)
    totalsulfurdioxide=models.FloatField(max_length=10)
    density=models.FloatField(max_length=10)
    pH=models.FloatField(max_length=10)
    sulphates=models.FloatField(max_length=10)
    alcohol=models.FloatField(max_length=10)

    def __str__(self):
        return self.alcohol