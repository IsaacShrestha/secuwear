from django.db import models

# Create your models here.

class CollectedData(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	temperature = models.CharField(max_length=500)
	def __unicode__(self):
		return str(self.temperature)
