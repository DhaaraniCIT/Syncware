from django.db import models

# Create your models here.
class device(models.Model):
	device_name =models.CharField(max_length=100)
	signal=models.CharField(max_length=1000)
	relationTootherDevice=models.CharField(max_length=1000)
	id=models.IntegerField(primary_key=True)
	class Meta:
		managed = False
		db_table="device"
class sample(models.Model):
	name =models.CharField(max_length=100)
	class Meta:
		managed = False
		db_table="sample"
		