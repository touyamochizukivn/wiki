from django.shortcuts import render, HttpResponse

# Create your views here.
def ts(request):
    return render(request, 'index.html')