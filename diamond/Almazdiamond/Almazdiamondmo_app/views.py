from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
#Create your views here.
def test_view(request):
    return render(request,'Homemain.html')

def test_2(request):
    return HttpResponse('working')
def login(request):

    return render(request,'login.html')
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def ring_settings_admin(request):
    ring_settings=RingSettings.objects.all()
    context={'ring_settings':ring_settings}
    return render(request,'ring_settings_admin.html',context)

def add_edit_ring_settings(request,id=None):
    ring_settings=ring_details=None
    if request.method=='POST':
        defaults={
            "ring_settings":request.POST.get('ring_settings',''),
            "metal_type":request.POST.get('metal_type',''),
            "shapes":request.POST.get('shapes',''),
            "name":request.POST.get('name',''),
            "description":request.POST.get('description',''),
            "price":request.POST.get('price',0),
            'currency':request.POST.get('currency','USD'),
           
        }
        if request.FILES.get('image'):
            defaults["image"]=request.FILES.get('image')
        ring,created=RingSettings.objects.update_or_create(
            id=id,
            defaults=defaults
        )
        if ring:
            files=request.FILES.getlist('files',[])
            for i in files:
                RingDetails.objects.create(
                    ring=ring,
                    file=i
                )

        return redirect('ring_settings_admin')
    if id:
        ring_settings=RingSettings.objects.filter(id=id).first()
        if ring_settings:
            ring_details=RingDetails.objects.filter(ring=ring_settings)
    return render(request,'add_edit_ring_setting.html',{"ring_settings":ring_settings,"setting_types":SETTING_TYPES,"metal_types":METAL_TYPES,"ring_shapes":RING_SHAPES,"currency":CURRENCY_CHOICES,"ring_details":ring_details,"id":id})

def delete_ring_setting(request,id):
    RingSettings.objects.filter(id=id).delete()
    return redirect('ring_settings_admin')

def delete_ring_files(reques,rs_id,id=None):
    if rs_id and id:
        ringdetails=RingDetails.objects.filter(ring_id=rs_id,id=id).first()
        if ringdetails:
           ringdetails.delete()
    elif rs_id:
        ring_settings=RingSettings.objects.filter(id=rs_id).first()
        if ring_settings:
            ring_settings.image=None
            ring_settings.save()
    return redirect(reverse('edit_ring',kwargs={"id":rs_id}))

def stone_admin(request):
    stone_details=StoneDetails.objects.filter.all()
    context={'stone_details':stone_details}
    return render(request,'stone_admin.html',context)
           