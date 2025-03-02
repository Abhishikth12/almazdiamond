from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from .serializers import *
# from rest_framework.response import Response
# import requests
from django.db.models import Q
from  Almazdiamond.settings import *
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
    return render(request,'ring_setting_admin.html',context)

def add_edit_ring_settings(request,id=None):
    ring_settings=None
    if request.method=='POST':
        defaults={
            "name":request.POST.get('name',''),
            "description":request.POST.get('description','')
        }
        
        ring,created=RingSettings.objects.update_or_create(
            id=id,
            defaults=defaults
        )
        return redirect('ring_settings_admin')
    if id:
        ring_settings=RingSettings.objects.filter(id=id).first()
        
    return render(request,'add_edit_ring_setting.html',{"ring_settings":ring_settings,"setting_types":SETTING_TYPES,"metal_types":METAL_TYPES,"ring_shapes":RING_SHAPES,"currency":CURRENCY_CHOICES,"id":id})
def ring_setting_variant_admin(request,ring_id):
    ring_setting_variants=Ring_setting_variants.objects.filter(ring_id=ring_id)
    ring_setting=RingSettings.objects.filter(id=ring_id).first()
    print(ring_setting_variants,"ring_setting_variants")
    return render(request,'ring_setting_variant_admin.html',{"ring_setting_variants":ring_setting_variants,"ring_setting":ring_setting})
def add_edit_ring_setting_variant(request,ring_id,id=None):
    ring_variant=ring_details=None
    if request.method=='POST':
        if ring_id:
            defaults={
            "price":request.POST.get('price',0),
            'currency':request.POST.get('currency','USD'),
            'ring_id':ring_id,
            'ring_settings':request.POST.get('ring_settings',''),
            'metal_type':request.POST.get('metal_type',''),
            'shapes':request.POST.get('shapes','')
            }
            if request.FILES.get('image'):
                defaults["image"]=request.FILES.get('image')
            variant,created=Ring_setting_variants.objects.update_or_create(
                    id=id,
                    defaults=defaults

            )
            if variant:
                files=request.FILES.getlist('files',[])
                for i in files:
                    RingDetails.objects.create(
                        ring_variant=variant,
                        file=i
                    )

        return redirect(reverse('ring_settings_variant_admin',kwargs={"ring_id":ring_id}))
    if id:
        ring_variant=Ring_setting_variants.objects.filter(id=id).first()
        if ring_variant:
            ring_details=RingDetails.objects.filter(ring_variant=ring_variant)

    ring_setting=RingSettings.objects.filter(id=ring_id).first()
    return render(request,'add_edit_ring_setting_variant.html',{"ring_setting":ring_setting,"ring_variant":ring_variant,"setting_types":SETTING_TYPES,"metal_types":METAL_TYPES,"ring_shapes":RING_SHAPES,"currency":CURRENCY_CHOICES,"ring_details":ring_details,"id":id})

def delete_ring_setting(request,id):
    RingSettings.objects.filter(id=id).delete()
    return redirect('ring_settings_admin')
def delete_ring_setting_variant(request,ring_id,id):
    Ring_setting_variants.objects.filter(id=id).delete()
    return redirect(reverse('ring_settings_variant_admin',kwargs={'ring_id':ring_id}))
def delete_ring_files(reques,rs_id,id=None):
    ring_id=None
    if rs_id and id:
        ringdetails=RingDetails.objects.filter(ring_variant=rs_id,id=id).first()
        if ringdetails:
            ring_id=ringdetails.ring_variant.ring_id
            ringdetails.delete()
    elif rs_id:
        ringsettingvariant=Ring_setting_variants.objects.filter(id=rs_id).first()
        if ringsettingvariant:
            ring_id=ringsettingvariant.ring_id

            ringsettingvariant.image=None
            ringsettingvariant.save()
    return redirect(reverse('edit_ring_variant',kwargs={"ring_id":ring_id,"id":rs_id}))

def stone_admin(request):
    stones=Stone.objects.all()
    context={'stones':stones}
    return render(request,'stone_admin.html',context)

def add_edit_stone(request,id=None):
    stone=stone_details=None
    if request.method=='POST':
        defaults={
            "stone_name":request.POST.get('stone_name',''),
            "description":request.POST.get('description',''),
            "stone_type":request.POST.get('stone_type',''),
            "stone_shape":request.POST.get('stone_shape',''),
            "stone_carat":14,
            "stone_price":request.POST.get('stone_price',0),
            "stone_cut":request.POST.get('stone_cut',''),
            "stone_clarity":request.POST.get('stone_clarity',""),
            'currency':request.POST.get('currency','USD')
           
        }
        if request.FILES.get('image'):
            defaults["image"]=request.FILES.get('image')
        stone,created=Stone.objects.update_or_create(
            id=id,
            defaults=defaults
        )
        if stone:
            files=request.FILES.getlist('files',[])
            for i in files:
                StoneDetails.objects.create(
                    stone=stone,
                    file=i
                )

        return redirect('stone_admin')
    if id:
        stone=Stone.objects.filter(id=id).first()
        if stone:
            stone_details=StoneDetails.objects.filter(stone=stone)
    return render(request,'add_edit_stone.html',{"stone":stone,"stone_cuts":STONE_CUT_CHOICES,"stone_clarities":STONE_CLARITY,"stone_shapes":STONE_SHAPES,"currency":CURRENCY_CHOICES,"stone_details":stone_details,"id":id})

def delete_stone(request,id):
    Stone.objects.filter(id=id).delete()
    return redirect('stone_admin')

def delete_stone_files(request,s_id,id=None):
    if s_id and id:
        stonedetails=StoneDetails.objects.filter(stone_id=s_id,id=id).first()
        if stonedetails:
           stonedetails.delete()
    elif s_id:
        stone=Stone.objects.filter(id=s_id).first()
        if stone:
            stone.image=None
            stone.save()
    return redirect(reverse('edit_stone',kwargs={"id":s_id}))

def ring_stone_combination_admin(request):
    combinations=Combination.objects.all()
    print(combinations,"lll")
    context={"combinations":combinations}
    return render(request,'combination_admin.html',context)
def add_edit_combination(request,id=None):
    combination=combination_files=None
    if request.method=='POST':
        defaults={
            "ring_id":request.POST.get('ring_id'),
            "stone_id":request.POST.get('stone_id'),
            "price":request.POST.get('price',0.0),
            "currency":request.POST.get('currency','USD')
        }
        combination,created=Combination.objects.update_or_create(
            id=id,
            defaults=defaults

        )
        if combination:
            files=request.FILES.getlist('files',[])
            for i in files:
                CombinationFiles.objects.create(
                    combination_id=combination.id,
                    files=i
                )
        return redirect('ring_stone_combination_admin')
    if id:
        combination=Combination.objects.filter(id=id).first()
        if combination:
            combination_files=CombinationFiles.objects.filter(combination_id=combination.id)
    stones=Stone.objects.all().only('id','stone_name')
    ring_settings=RingSettings.objects.all().only('id','name')
    print(ring_settings,stones,"lll")
    context={
        "combination_files":combination_files,
        "combination":combination,
        "id":id,
        "stones":stones,
        "ring_settings":ring_settings,
        "currency":CURRENCY_CHOICES
    }
    return render(request,'add_edit_combination.html',context) 

def delete_combination(request,id):
    combination=Combination.objects.filter(id=id).first()
    if combination:
        combination.delete()
    return redirect('ring_stone_combination_admin')

def delete_combination_files(request,c_id,id):
    if c_id and id:
        combinationfile=CombinationFiles.objects.filter(combination_id=c_id,id=id).first()
        if combinationfile:
            combinationfile.delete()
    return redirect(reverse('edit_combination',kwargs={"id":c_id}))

# def ring_setting_api(request,varient_id=None):
#     api_url = f"{DomainName}api/ring_setting_filter_api"
#     params = {}
#     if request.GET.get('ring_settings'):
#         params['ring_settings'] = request.GET['ring_settings']
#     if request.GET.get('metal_type'):
#         params['metal_type'] = request.GET['metal_type']
#     if request.GET.get('shapes'):
#         params['shapes'] = request.GET['shapes']
#     if request.GET.get('price_min'):
#         params['price_min'] = request.GET['price_min']
#     if request.GET.get('price_max'):
#         params['price_max'] = request.GET['price_max']
#     if request.GET.get('currency'):
#         params['currency'] = request.GET['currency']
#     if varient_id:
#         params['varient_id']=varient_id

#     # Call the API
#     response = requests.get(api_url, params=params)
#     return response
def ring_settings(request,stone_id=None):
    ring_variants=Ring_setting_variants.objects.all()
    if 'ring_settings' in request.GET:
        ring_variants=ring_variants.filter(ring_settings=request.GET['ring_settings'])
    return render(request,'setting.html',{"ring_variants":ring_variants,"settings":SETTING_TYPES,"stone_id":stone_id})

def get_more_ring_details(request, id=None, stone_id=None):
    # ring = get_object_or_404(RingSettings, id=id)  # Fetch ring or return 404
    # response=ring_setting_api(request,id)
    # if response.status_code == 200:
    #     ring_variants = response.json()  # API returns JSON response
    #     ring_details = RingDetails.objects.filter(ring_variant_id=id)

    #     print(ring_variants,"ring_variantsasasasa")
    print(id,stone_id,";lllll")
    selected_variant_ring=ring_variants=shapes=metal_types=setting_types=None
    if id:
        selected_variant_ring=Ring_setting_variants.objects.filter(id=id).first()
        ring_variants=Ring_setting_variants.objects.filter(ring=selected_variant_ring.ring.id)
        setting_types=ring_variants.values_list('ring_settings',flat=True).distinct()
        metal_types=ring_variants.values_list('metal_type',flat=True).distinct()
        shapes=ring_variants.values_list('shapes',flat=True).distinct()
    else:
        query=Q(ring_id=request.GET['ring_id'])
        print(request.GET,"request.GET")
        if 'style' in request.GET :
            query&= Q(ring_settings=request.GET['style']) 
            setting_types=Ring_setting_variants.objects.filter(ring_id=request.GET['ring_id']).values_list('ring_settings',flat=True).distinct()
        elif 'material' in request.GET :
            query&= Q(metal_type=request.GET['material']) 
            metal_types=Ring_setting_variants.objects.filter(ring_id=request.GET['ring_id']).values_list('metal_type',flat=True).distinct()
            print(metal_types,"klklk")
        elif 'shapes' in request.GET :
            print(request.GET['shapes'],"aaaaa")
            query&= Q(shapes=request.GET['shapes']) 
            shapes=Ring_setting_variants.objects.filter(ring_id=request.GET['ring_id']).values_list('shapes',flat=True).distinct()
        
        if query:
            print(query,"cccc")
            ring_variants=Ring_setting_variants.objects.filter(query)
            if shapes:
                setting_types=ring_variants.values_list('ring_settings',flat=True).distinct()
                metal_types=ring_variants.values_list('metal_type',flat=True).distinct()
            elif metal_types:
                setting_types=ring_variants.values_list('ring_settings',flat=True).distinct()
                shapes=ring_variants.values_list('shapes',flat=True).distinct()
            elif setting_types:
                metal_types=ring_variants.values_list('metal_type',flat=True).distinct()
                shapes=ring_variants.values_list('shapes',flat=True).distinct()
            print(ring_variants,"ring_variants")
            selected_variant_ring=ring_variants.first()
    
   
    ring_details=RingDetails.objects.filter(ring_variant=selected_variant_ring)
    return render(
        request,
        "ring_details.html",
        {
            "ring_details": ring_details,
            "ring": selected_variant_ring,
            "ring_shapes": shapes,   # ✅ Already present
            "metal_types": metal_types,   # ✅ Added this
            "setting_types": setting_types,  # ✅ Added this
            "stone_id": stone_id
        },
    )
def combination_stone_ring(request,stone_id,ring_id):
    # ring_id=Ring_setting_variants.objects.filter(ring_id=ring_id).first().ring_id
    combination=Combination.objects.filter(stone_id=stone_id,ring_variant_id=ring_id).first()
    combination_details=CombinationFiles.objects.filter(combination_id=combination)
    print(combination_details,"lll")
    return render(request,'combination_stone_ring.html',{"combination":combination,"combination_details":combination_details,"stone_id":stone_id,"ring_id":ring_id})

def stones(request,ring_id=None):
    stones=Stone.objects.all()
    query=Q()
    if 'stone_shape' in request.GET:
        query&=Q(stone_shape__icontains=request.GET['stone_shape'])
    if 'stone_clarity' in request.GET:
        query&=Q(stone_clarity__icontains=request.GET['stone_clarity'])
    if 'stone_cut' in request.GET:
        query&=Q(stone_cut__icontains=request.GET['stone_cut'])
    if query:
        print(query,"query")
        stones=Stone.objects.filter(query)
        print(stones,"stones")

    return render(request,'stone.html',{"stones":stones,"ring_id":ring_id,"stone_shapes":STONE_SHAPES,"stone_cuts":STONE_CUT_CHOICES,"stone_clarity":STONE_CLARITY})

def get_more_stone_details(request,id,ring_id=None):
    stone_details=StoneDetails.objects.filter(stone_id=id)
    print(stone_details,"mmm")
    stone=Stone.objects.filter(id=id).first()
    return render(request,'stone_details.html',{"stone_details":stone_details,"stone":stone,"stone_shapes":STONE_SHAPES,"ring_id":ring_id})



# @api_view(['GET'])
# def ring_setting_filter_api(request):
    query = Q()
    varient_id=None
    rings=serializer=None
    if 'ring_settings' in request.GET:
        query &= Q(ring_settings=request.GET['ring_settings', 'Solitaire'])
    if 'metal_type' in request.GET:
        query &= Q(metal_type=request.GET['metal_type','White Gold'])
    if 'shapes' in request.GET:
        query &= Q(shapes=request.GET['shapes','Round'])
    if 'name' in request.GET:
        query &= Q(name__icontains=request.GET['name'])  # Partial match
    if 'description' in request.GET:
        query &= Q(description__icontains=request.GET['description'])
    if 'price_min' in request.GET:
        query &= Q(price__gte=request.GET['price_min'])
    if 'price_max' in request.GET:
        query &= Q(price__lte=request.GET['price_max'])
    if 'currency' in request.GET:
        query &= Q(currency=request.GET['currency'])
    if 'varient_id' in request.GET:
        varient_id=request.GET['varient_id']
    # Fetch results based on the filter
    print(query,"lllll")
    if query and varient_id:
        rings = Ring_setting_variants.objects.filter(query,id=varient_id)
        serializer = Ring_setting_variantsSerializer(rings, many=False)
    else:
        rings = Ring_setting_variants.objects.all()
        serializer = Ring_setting_variantsSerializer(rings, many=True)

    return Response(serializer.data)