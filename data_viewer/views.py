from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse

from .models import Microrequest, Entry
from .forms import MictorequestForm
from .matplot import plot_page


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
	context = {"micreq": micreq, "entries": entries, "fps" : micreq.delay * 1000, 
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
