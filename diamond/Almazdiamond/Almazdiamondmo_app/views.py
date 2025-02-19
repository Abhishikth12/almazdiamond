from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
#Create your views here.
def test_view(request):
    return render(request,'Homemain.html')

def test_2(request):
    return HttpResponse('working')
def login(request):

    return render(request,'login.html')
def admin_dashboard(request):
    context={"CURRENCY_CHOICES":CURRENCY_CHOICES}
    return render(request,'admin_dashboard.html',context)
def submit_product(request,id=None):
    print(request.POST,request.FILES,"llll")
    if request.method=='POST':
        defaults={
            "name":request.POST.get('name',''),
            "description":request.POST.get('description',''),
            "price":request.POST.get('price',0),
            'currency':request.POST.get('currency','USD'),
           
        }
        if request.FILES.get('main_image'):
            defaults["main_image"]=request.FILES.get('main_image')
        files=request.FILES.getlist('Files',[])
        product,created=Products.objects.update_or_create(
            id=id,
            defaults=defaults
        )
        if product:
            for i in files:
                ProductFiles.objects.create(
                    product=product,
                    files=i
                )

    return redirect('admin_dashboard')

def setting(request):
    products=Products.objects.all()
    context={"products":products}
    return render(request,'setting.html',context)
def stone(request):
    products=Products.objects.all()
    context={"products":products}
    return render(request,'stone.html',context)