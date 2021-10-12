from django.db import models
  
class Consommation(models.Model):
    power = models.FloatField()
    dt= models.DateTimeField()
    json_data = models.JSONField()
    installation_id=models.SmallIntegerField()

    
    class Meta:
        db_table = 'graphs_data'

 