from django.db import models

from Auth.models import User



class Area(models.Model):

    name = models.CharField(max_length=200)
    location = models.URLField()


    def save(self,*args, **kwargs):

        super(Area,self).save(*args, **kwargs)
        for i in range(1,11):
            slot = Slots.objects.create(area = self,number=i)
            slot.save()


    def __str__(self) -> str:
        return self.name
        



class Slots(models.Model):

    area = models.ForeignKey(Area,related_name='slots',on_delete=models.CASCADE)
    number = models.IntegerField()
    is_busy = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.area.name + "===> " + str(self.number)


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    slots = models.ForeignKey(Slots,on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)
    car_no = models.CharField(max_length=15,null=True,blank=True)
    payment_method = models.CharField(max_length=100,null=True,blank=True)
    is_vip = models.BooleanField(default=False)


class Config(models.Model):
    key = models.CharField(default="1234",max_length=200)
    per_hour = models.IntegerField(default=50)
    per_hour_vip = models.IntegerField(default=80)



class Cheakout(models.Model):

    phone = models.CharField(max_length=16,null=True,blank=True)
    payment_id = models.CharField(max_length=50,null=True,blank=True)
    total = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
