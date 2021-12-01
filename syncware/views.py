from django.shortcuts import render

# Create your views here.
from syncware.models import device


# Create your views here.

def display(request):
	st=device.objects.all() # Collect all records from table 
	# print(st[0].device_name)
	return render(request,'display.html',{'st':st})