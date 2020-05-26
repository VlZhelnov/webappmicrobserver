from django import forms
from .models import Microrequest
from django.core.exceptions import ValidationError

class MictorequestForm(forms.Form):
	title = forms.CharField(max_length=200)
	delay = forms.IntegerField()
	quantity = forms.IntegerField()

	def clean_delay(self):
		new_delay = self.cleaned_data['delay']
		print(type(new_delay))
		if new_delay < 1 or new_delay > 99999:
			raise ValidationError('Invalid delay (1 to 99999)')
		return new_delay

	def clean_quantity(self):
		new_quantity = self.cleaned_data['quantity']
		if new_quantity < 1 or new_quantity > 99999:
			raise ValidationError('Invalid quantity (1 to 99999)')
		return new_quantity

	def save(self):
		new_micreq = Microrequest.objects.create(
			title = self.cleaned_data['title'],
			delay = self.cleaned_data['delay'],
			quantity = self.cleaned_data['quantity']
		)
		return new_micreq
 
