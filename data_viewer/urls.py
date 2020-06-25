from django.urls import path
from . import views

urlpatterns = [
	path("viewer/", views.microrequests_list, name="microrequests_list_url"),
	path("micreq/create/", views.Microrequest_create.as_view(), name="microrequest_create_url"),
	path("micreq/<int:pk>/", views.microrequest_detail, name="microrequest_detail_url"),
	path('micreq/<int:pk>/delete/', views.microrequest_delete, name="microrequest_delete_url")
	]
	
