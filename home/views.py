from django.shortcuts import render, HttpResponse

# Create your views here.

def post_list(request):
	#if request.user.is_authenticated():
	 #   context = {
	  #     'isim': 'Barış',
	   # }
    
    


	return render(request,'blog/post_list.html', {})