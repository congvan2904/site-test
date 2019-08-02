from django.shortcuts import render

# Create your views here.
from django.http import HttpReSponse
def index(request):
	response=HttpReSponse()
	response.writelines("<h1>xin chao</h1>")
	response.write("Day la app home")
	return response
