from django.http import HttpResponse

from django.shortcuts import render
from .forms import InputForm
def index(request):
    return HttpResponse("Hello, I'm Himanshu Gupta")



# Create your views here.
def home_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)
