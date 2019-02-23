from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from carshopapp.forms import UserForm, CarShopForm, UserFormForEdit, CarForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from carshopapp.models import Car

# Create your views here.
def home(request):
    return redirect(carshop_home)

@login_required(login_url='/carshop/sign-in/')
def carshop_home(request):
    return redirect(carshop_car)

@login_required(login_url='/carshop/sign-in/')
def carshop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    carshop_form = CarShopForm(instance=request.user.carshop)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        carshop_form = CarShopForm(request.POST, request.FILES, instance=request.user.carshop)

        if user_form.is_valid() and carshop_form.is_valid():
            user_form.save()
            carshop_form.save()

    return render(request, 'carshop/account.html', {
        'user_form': user_form,
        'carshop_form': carshop_form
    })

@login_required(login_url='/carshop/sign-in/')
def carshop_car(request):
    cars = Car.objects.filter(carshop=request.user.carshop).order_by("-id")
    return render(request, 'carshop/car.html', {
        'cars': cars
    })

@login_required(login_url='/carshop/sign-in/')
def carshop_add_car(request):
    form = CarForm()

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.carshop = request.user.carshop
            car.save()
            return redirect(carshop_car)

    return render(request, 'carshop/add_car.html', {
        'form': form
    })

@login_required(login_url='/carshop/sign-in/')
def carshop_edit_car(request, car_id):
    form = CarForm(instance=Car.objects.get(id=car_id))

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=Car.objects.get(id=car_id))
        if form.is_valid():
            car = form.save()
            return redirect(carshop_car)

    return render(request, 'carshop/edit_car.html', {
        'form': form
    })

def carshop_sign_up(request):
    user_form = UserForm()
    carshop_form = CarShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        carshop_form = CarShopForm(request.POST, request.FILES)

        if user_form.is_valid() and carshop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_carshop = carshop_form.save(commit=False)
            new_carshop.owner = new_user
            new_carshop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(carshop_home)

    return render(request, 'carshop/sign_up.html', {
        'user_form': user_form,
        'carshop_form': carshop_form
    })
