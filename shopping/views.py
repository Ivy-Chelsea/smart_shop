from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse

def index(request):
    category=Category.objects.filter()[:5]
    product=Item.objects.filter()[:5]#hello atom?? remember to put 8
    context={
        'category':category,
        'product':product,
    }
    return render(request, 'index.html', context)

def products(request,name):
    category=Category.objects.get(name=name)
    ids=category.id
    product=Item.objects.filter(category__exact=ids).values
    context={
        'product':product
    }
    return render(request, 'products.html',context)


def login(request):
    if request.method=='POST':
        username=request.POST['email']
        username=username
        password=request.POST['pwd']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            messages.info(request, 'Log in')
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

        
def signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        password2=request.POST['pwd2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=fname, last_name=lname,username=email, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            
            messages.info(request,'Password not same')
            return render(request, 'signup.html')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            messages.info(request,'Create your account')
            return render(request, 'signup.html') 

def order(request, name):
    if request.user.is_authenticated:
        item=Item.objects.get(name=name)
        context={
            'item':item,
        }
        return render(request, 'order.html',context)
    else:
        messages.info(request, 'Login to proceed with your order')
        return redirect('login')


def buy(request, name):
    if request.user.is_authenticated:
        item=Item.objects.get(id=name)
        itemname=item.name
        ordername=request.user.first_name
        email=request.user.email
        supply=Supplier(itemname=itemname, ordername=ordername, email=email)
        supply.save()       
        return redirect('myorder')
    else:
        messages.info(request, 'Login to proceed with your order')
        return redirect('login')

def myorder(request):
    if request.user.is_authenticated:
        pname=request.user.first_name
        data=Supplier.objects.filter(ordername=pname).values()
        context={
            'order':data
        }
        return render(request, 'myorders.html',context)
    else:
        messages.info(request, 'Login to view your order')
        return redirect('login')
    

def index(request):
    category=Category.objects.filter()[:5]
    category2=Category.objects.filter()
    product=Item.objects.filter()[:8]#hello atom??remember to put 8
    context={
        'category':category,
        'category2':category2,
        'product':product,
    }
    return render(request,'index.html',context)