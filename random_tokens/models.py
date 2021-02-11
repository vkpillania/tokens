from django.db import models
import time

# Create your models here.

class Tokens(models.Model):
    token      = models.CharField(primary_key=True, unique=True , max_length=100, null=False)
    is_block   = models.BooleanField( default=False)
    generated  = models.IntegerField(default = time.time )
    live_till  = models.IntegerField( null = True )

    class Meta:
        managed = True 
        db_table = 'tokens'
