from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def blah(request):
#     return HttpResponse('what?')

def uploads(request):
    return render(request, "uploads/uploads.html")

def singleUpload(request, pk):
    return render(request, "uploads/single-upload.html")

