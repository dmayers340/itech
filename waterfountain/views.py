from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext

def index(request):
	return render(request, 'index.html')

def about(request):
	return HttpResponse("About Page")

def findafountain(request):
	return HttpResponse("Find a Fountain")

def page_not_found(request):
	return render(request, '404.html')

def contact(request):
	return render(request, 'contact.html')


def search(request):
	return render(request, 'search.html')


