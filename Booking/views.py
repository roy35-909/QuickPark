from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.utils.timezone import utc
def areas(request):
    areas = Area.objects.all()
    context = {

        "area" : areas
    }

    print(areas.first().slots.all())
    return render(request,'area.html',context=context)




def bookarea(request,pk):

    if request.method == 'GET' :
        try:
            area = Area.objects.get(id=pk)
        except:
            return redirect('/book/areas')
        
        slots = Slots.objects.filter(area = area)
        
        context = {
            "area" : area,
            "slots" : slots
        }
        return render(request,'Book_slot.html',context=context)
    
    if request.method == 'POST':

        data = request.POST

        slot = data['slotNumber']
        car_no = data['carNumber']
        areas= Area.objects.get(id=pk)
        slot = Slots.objects.get(id=int(slot))
        if slot.is_busy:
            return redirect('/')

        obj = Booking.objects.create(user=request.user,area=areas,slots = slot,car_no = car_no)
        try:
            payment = data['checkbox1']
            obj.payment_method = "Nagad"
        except:
            payment = data['checkbox']
            obj.payment_method = "Bikash"
        try:
            vip = data['vip']
            obj.is_vip = True
        except:
            pass

        obj.save()
        slot.is_busy = True
        slot.save()

        return redirect('/')
    



def cheakout(request,pk):

    if request.method == 'GET':

        book = Booking.objects.get(id=pk)
        config = Config.objects.get(key="1234")
        now = datetime.utcnow().replace(tzinfo=utc)
        totaltime = now - book.start_time
        totaltime = totaltime.total_seconds()
      
        totaltimehour = totaltime/3600
        totaltimehour = round(totaltimehour,3)
        if book.is_vip:
            sub_total = totaltimehour*config.per_hour_vip
            sub_total = round(sub_total,3)
        else:
            sub_total = totaltimehour*config.per_hour
            sub_total = round(sub_total,3)
        if request.user.is_authenticated:

            return render(request,'cheakout.html',{"now":now.utcnow(),"booking":book,"time":totaltimehour,"subtotal":sub_total,"config":config})
        
        else:
            return redirect('/')
        

    if request.method == 'POST':
        data = request.POST
        phone = data['phone']
        trx_id = data['payment-id']
        total = data['total']
        print(total)
        booking = Booking.objects.get(id=pk)

        slot = Slots.objects.get(id = booking.slots.id)
        slot.is_busy = False
        slot.save()
        booking.end_time = datetime.utcnow().replace(tzinfo=utc)
        cheakout = Cheakout.objects.create(total = float(total), phone = phone,payment_id = trx_id,user = request.user)
        cheakout.save()
        booking.save()

        return redirect('/')
    

def cheakout_list(request):

    if request.method == 'GET':


        if request.user.is_authenticated:

            all_booking = Booking.objects.filter(user=request.user,end_time = None)

            return render(request,'cheakout_list.html',{'all_booking':all_booking})






