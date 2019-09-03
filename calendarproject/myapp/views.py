from django.shortcuts import render

def index(req):
  return render(req, 'myapp/index.html')

def myapp(req):
  return render(req, 'myapp/myapp.html')