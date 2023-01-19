from email import message
from os import stat
from django.shortcuts import render

from FlavourApp.models import User, Feedback, Item

def index(request):
    index_items = Item.objects.all()
    food_items = {'food' : index_items}
    return render(request, "FlavourApp/index.html", food_items)

def locator(request):
    return render(request, "FlavourApp/locator.html")

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("mobile", "")
        msg = request.POST.get("message", "")
        feed = Feedback(name=name, email=email, mobile=phone, message=msg)
        feed.save()
    return render(request, "FlavourApp/feedback.html")

def register(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("confirm", "")
        reg = User(name=name, email=email, password=password)
        reg.save()
    return render(request, "FlavourApp/register.html")

def login(request):
    if request.method == "POST":
        log_email = request.POST["log_email"]
        log_pass = request.POST["log_pas"]
        log_det = User.objects.all()
        for users in log_det:
            if users.email == log_email and users.password == log_pass:
                return render(request, "FlavourApp/index.html")
    return render(request, "FlavourApp/login.html")

def cart(request):
    return render(request, "FlavourApp/cart.html")

def orders(request):
    return render(request, "FlavourApp/orders.html")

def checkout(request):
    user_det = User.objects.all()
    user = None
    for users in user_det:
        if users.email == 'govindkushwaha0786@gmail.com':
            user = User.objects.get(id=users.id)
            break

    if request.method == "POST":
        area = request.POST.get("area", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        areaPin = request.POST.get("areaPin", "")
        phone = request.POST.get("phone", 0)
        if not area or not city or not state or not areaPin:
            print("Enter all details")
        
        elif user is not None:
            user.area = area
            user.city = city
            user.state = state
            user.areaPin = areaPin
            user.mobile = phone
            user.save()
    
    if user is not None:
        area = user.area
        city = user.city
        state = user.state
        areaPin = user.areaPin
        if not area or not city or not state or not areaPin:
            return render(request, "FlavourApp/checkout.html")

        else:
            user_det = User.objects.all()
            user = None
            for users in user_det:
                if users.email == 'govindkushwaha0786@gmail.com':
                    user = User.objects.get(id=users.id)
                    break
            user_address = {'user' : user}
            return render(request, "FlavourApp/checkoutAdd.html", user_address)

    return render(request, "FlavourApp/checkout.html")

def updater(request):
    user_det = User.objects.all()
    user = None
    for users in user_det:
        if users.email == 'govindkushwaha0786@gmail.com':
            user = User.objects.get(id=users.id)
            break
    user.area = ""
    user.city = ""
    user.state = ""
    user.areaPin = ""
    user.mobile = 0
    user.save()

    return render(request, "FlavourApp/checkout.html")


def handler(request):
    
    return render(request, "FlavourApp/handler.html")
