from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

from shop import models
from shop.models import category, Product, cart, contacts


def home(request):
    cats = category.objects.all()
    pro = Product.objects.all()
    pro = (pro[::-1])
    return render(request, "home.html", {'cats': cats, 'pro': pro})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def docontact(request):
    name = request.POST['name']
    email = request.POST['email']
    sub = request.POST['subject']
    msg = request.POST['message']
    con = contacts.objects.create(name=name, email=email, sub=sub, msg=msg)
    con.save();
    return redirect("/")


def dosignup(request):
    username = request.POST['username']
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    pwd = request.POST['password']
    cpwd = request.POST['cpassword']
    if pwd == cpwd:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect("/signup")
        else:
            user = User.objects.create_user(username=username, password=pwd, email=email, first_name=first,
                                            last_name=last)
            user.save();
            return redirect("/")
    else:
        return render(request, "signup.html")


def signup(request):
    return render(request, "signup.html")


def signin(request):
    return render(request,'login.html')



def signincheck(request):
    password = request.POST['password']
    username = request.POST['username']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect("/")
    else:
        messages.info(request, 'Invalid Username or Password')
        return redirect("/signin")


def signout(request):
    auth.logout(request)
    return redirect("/")


def gallery(request):
    pro = Product.objects.all()
    return render(request, "gallery.html", {'pro': pro})


def single(request, pid):
    cats = category.objects.all()
    pro = Product.objects.get(id=pid)
    return render(request, "single.html", {'cats': cats, 'pro': pro})


def addcart(request, gid):
    pro = Product.objects.get(id=gid)
    qty = request.POST['qty']
    username = str(request.user)
    prod = cart.objects.create(p_user=username, p_name=pro.p_name, p_price=pro.p_price, p_qty=qty, p_img=pro.p_img)
    prod.save()
    return redirect("/cartdetail")


def cartdetail(request):
    username = request.user
    pro = list(cart.objects.all().filter(p_user=username, p_status=False))
    add = 0
    for i in pro:
        add = add + i.p_price * i.p_qty
    return render(request, "cart.html", {'pro': pro, 'add': add})


def checkout(request):
    username = request.user
    cart.objects.all().filter(p_user=username).update(p_status=True)
    return redirect("/")


def removecart(request, rid):
    username = request.user
    cart.objects.all().filter(p_user=username, id=rid).delete()
    return redirect("/cartdetail")


def myorder(request):
    username = request.user
    pro = list(cart.objects.all().filter(p_user=username, p_status=True, p_admin_status=False))
    con = list(cart.objects.all().filter(p_user=username, p_status=True, p_admin_status=True))
    return render(request, "myorder.html", {'pro': pro, 'con': con})
