from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Create your views here.
def test_view(request):
    return render(request,'test.html')

def test_2(request):
    return HttpResponse('working')