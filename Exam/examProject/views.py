from django.shortcuts import render

def index(request):
    return render(request,'homepage.html')
def about(req):
	return render(req,'about.html')
def contact(req):
	return render(req,'contact.html')