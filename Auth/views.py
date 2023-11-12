from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import User
from django.contrib import messages
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request,'login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        nid = request.POST['nid']
        password = request.POST['password']

        print(email)
        print(password)
        print(type(nid))

        if email == '':
            try:
                u = User.objects.get(nid=str(nid))
            
            except:            
                messages.error(request,"NID Not found.")
                return redirect('/auth/login')
            
            email = u.email
        user = auth.authenticate(email=email,password = password)
        if user is not None:
            auth.login(request,user)

        else:
            messages.error(request,"User Not found.")
            return redirect('/auth/login')

        return redirect('/')


def register(request):

    if request.method == 'GET':
        if request.user.is_superuser == False:
            if request.user.is_authenticated == False:
                return render(request,'reg.html')
            
            else:
                return redirect('/')
        else:
            return render(request,'reg.html')
    
    elif request.method == 'POST':



        data = request.POST
        try:

            email = data['email']
        except:
            email = ''
        nid = data['nid']
        first_name = data['first_name']
        last_name = data['last_name']
        phone = data['phone']
        password = data['password']
        if User.objects.filter(email = email).exists():
            messages.error(request,"Email Already Exist.")
            return redirect('/auth/register')
        if nid!='':
            if User.objects.filter(nid = str(nid)).exists():
                messages.error(request,"NID Already Exist.")
                return redirect('/auth/register')
        if email=='':
            if nid=='':
                messages.error(request,"Give NID OR Email .")
                return redirect('/auth/register')
            else:
                email = "employee"+str(nid)+"@quickpark.com"
        user = User.objects.create(email = email,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.phone = phone
        if nid!='':
            user.nid = nid

        if request.user.is_superuser:
            user.is_staff = True
            user.save()
            messages.success(request,"{} user Created".format(user.email))
            return redirect('/auth/register')
        user.save()
        return redirect('/auth/login')



def logout(request):

    auth.logout(request)
    return redirect('/')