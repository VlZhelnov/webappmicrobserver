from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Microrequest(models.Model):
	STATUS_CHOICES = [
		("adopted", "adopted"),
		("processing", "processing"),
		("completed", "completed"),
		("error", "error"),
	]
	title = models.CharField(max_length=200, db_index=True, db_column = "title")
	data_request = models.DateTimeField(auto_now_add=True, db_column = "data_request")
	data_accept = models.DateTimeField(blank=True, null=True, db_column = "data_accept")
	data_completed = models.DateTimeField(blank=True, null=True, db_column = "data_completed")
	delay = models.PositiveIntegerField(db_column = "delay")
	quantity = models.PositiveIntegerField(db_column = "quantity")
	status =  models.CharField(max_length=10, choices=STATUS_CHOICES, default = "adopted", db_column = "status")
	
	def get_absolute_url(self):
	        return reverse('microrequest_detail_url', kwargs={"pk":self.pk})
	def __str__(self):
		return self.title
	class Meta:
	        db_table = 'microrequest'
	

class Entry(models.Model):
	interval = models.IntegerField(db_column = "elapsed_time")
	temperature = models.SmallIntegerField(db_column = "temperature")
	illumination = models.SmallIntegerField(db_column = "illumination")
	microrequest =  models.ForeignKey("Microrequest", on_delete=models.CASCADE, related_name="microrequest_id")

	class Meta:
	        db_table = 'entry'

