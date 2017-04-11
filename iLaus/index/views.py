from django.shortcuts import render

# Create your views here.

def index_handler(req):
	return render(req, "index/index.html")
