from django.shortcuts import render, redirect
from .models import Microrequest, Entry
from .forms import MictorequestForm
from django.views.generic import View
from django.http import JsonResponse


import matplotlib 
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
import io
import urllib, base64
import datetime, time
import numpy as np

def plot_page(entries, start_time):
	interval = entries.values_list('interval')      
	temp = entries.values_list('temperature')
	light = entries.values_list('illumination')

	interval = np.array([start_time + i[0] for i in interval])  
	temp = np.array([t[0] for t in temp])
	light = np.array([l[0] for l in light])

	fig = Figure(figsize=(10,10), constrained_layout=True, dpi=100)
	axs = fig.subplots(2,1)
	axs[0].plot_date(interval, temp, 'r-', xdate=True, tz='Europe/Moscow')
	axs[1].plot_date(interval, light, 'y-', xdate=True, tz='Europe/Moscow')
	axs[0].set_title('Ambient temperature') 
	axs[1].set_title('Degree of illumination')      
	buf = io.BytesIO()
	fig.savefig(buf, format = 'png')
	string =  base64.b64encode(buf.getbuffer()).decode("ascii")
	uri = urllib.parse.quote(string)
	return uri


def microrequests_list(request):
	micreqs = Microrequest.objects.all()
	return render(request, 'index.html', context={"micreqs": micreqs})

def microrequest_detail(request, pk):
	micreq = Microrequest.objects.get(pk=pk)
	entries = Entry.objects.filter(microrequest_id=pk)
	if request.is_ajax():
		context = {"uri":plot_page(entries, micreq.data_accept), "status": micreq.status,
				   "count":entries.count()}
		return JsonResponse(context, status=200)
	contexti = {"micreq": micreq, "entries": entries, "fps" : micreq.delay * 1000, 
			 	"uri":plot_page(entries, micreq.data_accept)}
	return render(request, 'detail.html',context=context) 



def microrequest_delete(request, pk):
	entries = Entry.objects.filter(microrequest_id=pk)
	micreq = Microrequest.objects.get(pk=pk)
	entries.delete()
	micreq.delete()
	return redirect("microrequests_list_url")

class Microrequest_create(View):
	def get(self, request):
		form = MictorequestForm()
		return render(request, 'create.html', context={"form": form})
	def post(self, request):
		bound_form = MictorequestForm(request.POST)
		if bound_form.is_valid():
			new_micreq = bound_form.save()
			return redirect(new_micreq)
		return render(request, 'create.html', context={"form": bound_form})
