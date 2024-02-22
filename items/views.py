from django.shortcuts import render, HttpResponse
# Create your views here.
def itemsTest(request):
    return render(request, 'items/itemsIndex.html')