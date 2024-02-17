from django.shortcuts import render

# Create your views here.
def url1(request):
    return render(request,'web.html')
def url(request):
    return render(request,'index.html')