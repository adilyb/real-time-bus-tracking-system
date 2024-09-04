from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Location
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your views here.

@login_required
@csrf_exempt
def home_redirect(request):
    user = request.user
    try:
        profile = user.userprofile
    except ObjectDoesNotExist:
        # Handle the case where UserProfile doesn't exist
        # Redirect, create the profile, or return an error
        return redirect('login')  # or some other action
    

    if request.user.userprofile.role == 'driver':
        return render(request, 'bts_app/driver.html')
    elif request.user.userprofile.role == 'office':
                return render(request, 'bts_app/office.html')

    elif request.user.userprofile.role == 'admin':
        return redirect('admin_home')
    else:
        # Default redirect or handle unknown role
        return redirect('login')

@login_required
def index(request):
    return render(request, 'bts_app/index.html')  

@login_required
def driver(request):
    return render(request, 'bts_app/driver.html')  

@login_required
def office(request, id):
    return render(request, 'bts_app/office.html', {'id': id})  



def location_save(request):
    if request.method == "POST" :
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        user = request.user 

        Location.objects.create(user=user, latitude=latitude, longitude=longitude)

        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{user.id}',
            {
                'type': 'location_update',
                'latitude': latitude,
                'longitude': longitude,
            }
        )

        return redirect('/')
    

