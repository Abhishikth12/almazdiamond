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
import json
#Create your views here.
def test_view(request):
    return render(request,'Homemain.html')

def test_2(request):
    return HttpResponse('working')
def login(request):

    return render(request,'login.html')
def admin_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect("admin_login")

    return render(request, "admin_dashboard.html")

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
    ring_variant=ring_details_file=ring_details_360=None
    if request.method=='POST':
        if ring_id:
            defaults={
            "price":request.POST.get('price',0),
            'currency':request.POST.get('currency','USD'),
            'ring_id':ring_id,
            'ring_settings':request.POST.get('ring_settings',''),
            'metal_type':request.POST.get('metal_type',''),
            'shapes':request.POST.get('shapes',''),
            "carat":request.POST.get('carat','14k'),
            "width":request.POST.get('width',''),
            "profile":request.POST.get('profile','')
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
                file_360=request.FILES.getlist('files_360',[])
                for i in file_360:
                    RingDetails.objects.create(
                        ring_variant=variant,
                        ring_images_360=i
                    )

        return redirect(reverse('ring_settings_variant_admin',kwargs={"ring_id":ring_id}))
    if id:
        ring_variant=Ring_setting_variants.objects.filter(id=id).first()
        if ring_variant:
            ring_details_file = RingDetails.objects.filter(
                ring_variant=ring_variant
            ).exclude(file="").only("ring_variant", "id", "file")

            print(ring_details_file,"ring_details_file")
            for i in ring_details_file:
                print(i.file,"lll")
            ring_details_360=RingDetails.objects.filter(ring_variant=ring_variant).exclude(ring_images_360='').only('ring_variant','id','ring_images_360')
            print(ring_details_360,"ring_details_360")
    ring_setting=RingSettings.objects.filter(id=ring_id).first()
    return render(request,'add_edit_ring_setting_variant.html',{"ring_setting":ring_setting,"ring_variant":ring_variant,"setting_types":SETTING_TYPES,"metal_types":METAL_TYPES,"ring_shapes":RING_SHAPES,"currency":CURRENCY_CHOICES,"ring_details_file":ring_details_file,"ring_details_360":ring_details_360,"id":id})

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
            file_360=request.FILES.getlist('files_360',[])
            for i in file_360:
                StoneDetails.objects.create(
                    stone=stone,
                    stone_images_360=i
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
    print(request.body,"lll")
   
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            print(data,"data")
            # {'metal': 'Yellow Gold', 'shape': 'Pear', 'price_sort': 'High to Low', 'ringCategory': 'Halo'}
            ring_variants=Ring_setting_variants.objects.filter(metal_type=data['metal'],shapes=data['shape'],ring_settings=data['ringCategory'])
            if data['price_sort']=='High to Low':
                print('High to Low')
                ring_variants=ring_variants.order_by('-price')
            elif data['price_sort']=='Low to High':
                print('Low to High')
                ring_variants=ring_variants.order_by('price')
            print(ring_variants,"ring_variants_queryset")
            if ring_variants.exists():
                ring_variants_list = list(ring_variants.values(
                'id', 'ring_settings', 'metal_type', 'shapes', 'price', 'currency', 'image',
                'ring__id', 'ring__name', 'ring__description'  # Include fields from the related RingSettings model
            ))
                print(ring_variants_list,"ring_variants")
                return JsonResponse({"message": "Data received", "data": ring_variants_list,"stone_id":stone_id})
            else:
                return JsonResponse({"message": "Data received", "data": []})

        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    if stone_id:
        cart,created=Cart.objects.update_or_create(
            stone_id=stone_id,
            defaults={"item_count": 1} 
        )
    

        if not created:
            cart.item_count += 1
            cart.save()

    ring_variants=Ring_setting_variants.objects.filter(metal_type='White Gold',shapes='Round',ring_settings='Solitaire').order_by('-price')
    
    return render(request,'setting.html',{"ring_variants":ring_variants,"settings":SETTING_TYPES,"metal_types":METAL_TYPES,"ring_shapes":RING_SHAPES,"stone_id":stone_id})

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
    # combination=Combination.objects.filter(stone_id=stone_id,ring_variant_id=ring_id).first()
    # if combination:
    #     ring_images=combination.ring_variant.ring_details.all()
    # combination_details=CombinationFiles.objects.filter(combination_id=combination)
    # print(combination_details,"lll")
    ring_variant=stone=None
    ring_variant=Ring_setting_variants.objects.filter(id=ring_id).first()
    if ring_variant:
        ring_details=RingDetails.objects.filter(ring_variant=ring_variant)
        if ring_details.exists():
            ring_details=ring_details[:2]
    stone=Stone.objects.filter(id=stone_id).first()
    if stone:
        stone_details=StoneDetails.objects.filter(stone=stone)
        if stone_details.exists():
            stone_details=stone_details[:2]
    ring_size = tuple(f"{x:.2f}".rstrip('0').rstrip('.') for x in [i * 0.25 for i in range(12, 44)])
    

    return render(request,'combination_stone_ring.html',{"ring_size":ring_size,"ring_variant":ring_variant,"stone":stone,"stone_details":stone_details,"ring_details":ring_details,"stone_id":stone_id,"ring_id":ring_id,"total":ring_variant.price+stone.stone_price})

def stones(request,ring_id=None):
   
    if request.method == "POST":
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            print(data,"data")
            # {'metal': 'Yellow Gold', 'shape': 'Pear', 'price_sort': 'High to Low', 'ringCategory': 'Halo'}
            stones=Stone.objects.filter(stone_type=data['stone_type'],stone_shape=data['stone_shape'],stone_carat=data['stone_carat'],stone_color=data['stone_color'],stone_clarity=data['stone_clarity'],stone_cut=data['stone_cut'])
            if stones['price_sort']=='High to Low':
                print('High to Low')
                stones=stones.order_by('-price')
            elif data['price_sort']=='Low to High':
                print('Low to High')
                stones=stones.order_by('price')
            print(stones,"stones")
            if stones.exists():
                stones_list = list(stones.values())
                print(stones_list,"stones_list")
                return JsonResponse({"message": "Data received", "data": stones_list,"ring_id":ring_id})
            else:
                return JsonResponse({"message": "Data received", "data": []})

        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    stones=Stone.objects.filter(stone_shape='Round').order_by('-stone_price')
    if ring_id:
        print(ring_id,"ring_id")
        cart, created = Cart.objects.get_or_create(
            ring_variant_id=ring_id,
            defaults={"item_count": 1}  # Set item_count to 1 if creating a new cart
        )

        if not created:
            cart.item_count += 1
            cart.save()


    return render(request,'stone.html',{"stones":stones,"ring_id":ring_id,"stone_shapes":STONE_SHAPES,"stone_cuts":STONE_CUT_CHOICES,"stone_clarity":STONE_CLARITY})

def get_more_stone_details(request,id,ring_id=None):
    stone_details=StoneDetails.objects.filter(stone_id=id)
    print(stone_details,"mmm")
    stone=Stone.objects.filter(id=id).first()
    return render(request,'stone_details.html',{"stone_details":stone_details,"stone":stone,"stone_shapes":STONE_SHAPES,"ring_id":ring_id})



# @api_view(['GET'])
# def ring_setting_filter_api(request):
    # query = Q()
    # varient_id=None
    # rings=serializer=None
    # if 'ring_settings' in request.GET:
    #     query &= Q(ring_settings=request.GET['ring_settings', 'Solitaire'])
    # if 'metal_type' in request.GET:
    #     query &= Q(metal_type=request.GET['metal_type','White Gold'])
    # if 'shapes' in request.GET:
    #     query &= Q(shapes=request.GET['shapes','Round'])
    # if 'name' in request.GET:
    #     query &= Q(name__icontains=request.GET['name'])  # Partial match
    # if 'description' in request.GET:
    #     query &= Q(description__icontains=request.GET['description'])
    # if 'price_min' in request.GET:
    #     query &= Q(price__gte=request.GET['price_min'])
    # if 'price_max' in request.GET:
    #     query &= Q(price__lte=request.GET['price_max'])
    # if 'currency' in request.GET:
    #     query &= Q(currency=request.GET['currency'])
    # if 'varient_id' in request.GET:
    #     varient_id=request.GET['varient_id']
    # # Fetch results based on the filter
    # print(query,"lllll")
    # if query and varient_id:
    #     rings = Ring_setting_variants.objects.filter(query,id=varient_id)
    #     serializer = Ring_setting_variantsSerializer(rings, many=False)
    # else:
    #     rings = Ring_setting_variants.objects.all()
    #     serializer = Ring_setting_variantsSerializer(rings, many=True)

    # return Response(serializer.data)

def addto_wishlist(request):
    if request.method=='POST':
        data = json.loads(request.body)
        print(data,"data")
        if 'ring_variant_id' in data:
            wishlist,created=Wishlist.objects.update_or_create(
                ring_variant_id =data['ring_variant_id']
            )
        if 'stone_id' in data:
            wishlist,created=Wishlist.objects.update_or_create(
                stone_id=data['stone_id']
            )
        return JsonResponse({"message": "Data received"})
    
def addto_cart(request):
    if request.method=='POST':
        data = json.loads(request.body)
        print(data,"data")
        if 'ring_variant_id' in data:
            cart,created=Cart.objects.get_or_create(
                ring_variant_id =data['ring_variant_id'],
                defaults={"item_count": 1} 
            )
           

            if not created:
                cart.item_count += 1
                cart.save()
        if 'stone_id' in data:
            cart,created=Cart.objects.update_or_create(
                stone_id=data['stone_id'],
                defaults={"item_count": 1} 
            )
           

            if not created:
                cart.item_count += 1
                cart.save()
            
        return JsonResponse({"message": "Data received"})

def view_cart(request):
    cart_list=Cart.objects.all()
    return render(request,'view_cart.html',{'cart_list':cart_list})

def view_wishlist(request):
    wishlist=Wishlist.objects.all()
    return render(request,'view_wishlist.html',{'wishlist':wishlist})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def admin_login(request):
    print("lll")
    if request.user.is_authenticated:  # If admin is already logged in
        print("autherized")
        return redirect("admin_dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Ensuring only admin can log in
            login(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid Credentials or Not an Admin")

    return render(request, "admin_login.html")


# def admin_dashboard(request):
#     if not request.user.is_authenticated or not request.user.is_staff:
#         return redirect("admin_login")

#     return render(request, "admin_dashboard.html")


def admin_logout(request):
    logout(request)
    return redirect("admin_login")
