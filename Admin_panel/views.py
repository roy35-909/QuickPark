from django.shortcuts import render,redirect
from Booking.models import *
from Auth.models import User
def dashboard(request):

    if request.user.is_superuser:

        all_booking = Booking.objects.filter(end_time = None)
        top_customer = User.objects.filter(is_staff = False)[:8]
        total_active_car = all_booking.count()
        total_slot = Slots.objects.all().count
        total_free_slot = Slots.objects.filter(is_busy = False).count()

        context = {
            "booking" : all_booking,
            "customer" : top_customer,
            "total_active_car" : total_active_car,
            "total_vip_car" : Booking.objects.filter(is_vip=True).count(),
            "total_slot": total_slot,
            "total_free_slot" : total_free_slot
        }

        return render(request,'dashboard.html',context=context)
    
    else:
        return redirect('/')
    

def dashboard_area(request):

    if request.user.is_superuser:

        areas = Area.objects.all()

        return render(request,'dashboard-area.html',{"areas":areas})
    else:
        return redirect('/')

def delete_area(request,pk):

    area = Area.objects.get(id=pk)

    slots = Slots.objects.filter(area=area)

    for i in slots:

        slots.delete()

    area.delete()

    return redirect('/dashboard/area')



def dashboard_slots(request):

    if request.user.is_superuser:

        area = Area.objects.all()
        return render(request,'dashboard_slots.html',{"areas":area})
    else:
        return redirect('/')
    

def dashboard_slot_action(request,pk,action):

    if request.user.is_superuser:
        area = Area.objects.get(id=pk)
        if action=="i":
            slots = Slots.objects.all().order_by('-number')[0].number
            slot = Slots.objects.create(area = area,number=slots+1)
            slot.save()
            return redirect('/dashboard/slots')
        if action=="d":
            slots = Slots.objects.all().order_by('-number')[0].number
            slot = Slots.objects.get(area=area,number=slots)
            slot.delete()
            return redirect('/dashboard/slots')
        
def dashboard_regiser_staff(request):


    if request.user.is_superuser:


        staff = User.objects.filter(is_superuser = False, is_staff = True)
        return render(request,'regester_staff.html',{"staff":staff})
    else:
        return redirect('/')
    

def delete_staff(request,pk):

    if request.user.is_superuser:

        staff = User.objects.get(id=pk)

        staff.delete()
        return redirect('/dashboard/regiser_staff')
    else:
        return redirect('/')
    

def dashboard_payment(request):


    if request.user.is_superuser:


        payment = Cheakout.objects.all().order_by('-id')[:20]
        return render(request,'dashboard_payment.html',{"cheakout":payment})
    else:
        return redirect('/')