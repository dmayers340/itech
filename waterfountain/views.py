from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext

def index(request):
	return render(request, 'findafountain/index.html')

def about(request):
	return render(request, 'findafountain/about.html')

def map(request):
	return render(request, 'findafountain/map.html')

def page_not_found(request):
	return render(request, HttpResponseNotFound, 'findafountain/404.html')

def contact(request):
	return render(request, 'findafountain/contact.html')


def search(request):
	return render(request, 'findafountain/search.html')


