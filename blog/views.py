from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def post_index(request):
	posts= Post.objects.all()
	return render(request, '/index.html', {'posts': posts})

def post_detail(request):
	return HttpResponse('Burası detail index sayfası')

def post_create(request):
	return HttpResponse('Burası create index sayfası')

def post_update(request):
	return HttpResponse('Burası update index sayfası')

def post_delete(request):
	return HttpResponse('Burası delete index sayfası')