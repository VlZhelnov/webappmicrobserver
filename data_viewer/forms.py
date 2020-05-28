from django import forms
from .models import Microrequest
from django.core.exceptions import ValidationError
from django.db.models import Sum

MAX_FREE_SPACE_DB = 10000

def correct_number(number):
	if number < 1 or number > 99999:
		raise ValidationError('Enter number 1 to 99999')
	return number
	


class MictorequestForm(forms.Form):
	title = forms.CharField(max_length=200)
	delay = forms.IntegerField()
	quantity = forms.IntegerField()

	def clean_delay(self):
		return correct_number(self.cleaned_data['delay'])

	def clean_quantity(self):
		new_quantity = correct_number(self.cleaned_data['quantity'])
		count_entries = Microrequest.objects.all().aggregate(Sum('quantity'))["quantity__sum"] or 0
		free = MAX_FREE_SPACE_DB - Microrequest.objects.count() - count_entries - 1
		if new_quantity > free:	
			raise ValidationError('Free server space '+ str(0 if free < 0 else free))
		return new_quantity

	def save(self):
		new_micreq = Microrequest.objects.create(
			title = self.cleaned_data['title'],
			delay = self.cleaned_data['delay'],
			quantity = self.cleaned_data['quantity']
		)
		return new_micreq
 
