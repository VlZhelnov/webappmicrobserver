from django.db import models

# Create your models here.

class Microrequest(models.Model):
	STATUS_CHOICES = [
		("adopted", "adopted"),
		("processing", "processing"),
		("completed", "completed"),
	]
	title = models.CharField(max_length=200, db_index=True)
	data_request = models.DateTimeField(auto_now_add=True)
	data_accept = models.DateTimeField(blank=True, null=True)
	delay = models.PositiveIntegerField()
	quantity = models.PositiveIntegerField()
	status =  models.CharField(max_length=10, choices=STATUS_CHOICES, default = "adopted")
	
	def __str__(self):
		return self.title
	

class Entry(models.Model):
	interval = models.DurationField()
	temperature = models.SmallIntegerField()
	illumination = models.SmallIntegerField()
	microrequest =  models.ForeignKey("Microrequest", on_delete=models.CASCADE, related_name="microrequest")

	

