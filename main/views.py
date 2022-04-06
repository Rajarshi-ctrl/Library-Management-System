from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout



def index(request):
    data = Book.objects.all()
    return render(request, 'index.html', {'data': data})


def dashboard(request):
    data = Book.objects.all()
    params = {'data': data}
    return render(request, 'dashboard.html', params)


def destroy(request, id):
    item = Book.objects.get(id=id)
    item.delete()
    return redirect("/dashboard")


def edit(request, id):
    item = Book.objects.get(id=id)
    return render(request, 'edit.html', {'item': item})


def update(request, id):
    item = Book.objects.get(id=id)
    form = BookForm(instance=item)
    if request.method == 'GET':
        form = BookForm(request.GET, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
    return render(request, 'edit.html', {'item': item})


def add(request):
    if request.method == "POST" and 'add' in request.POST:
        name = request.POST.get('name')
        auther = request.POST.get('auther')
        desc = request.POST.get('desc')
        book = Book(name=name, auther=auther, desc=desc)
        book.save()
    return redirect("dashboard")


def userlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                messages.success(request, 'Welcome to Dashboard.')
                return redirect("dashboard")
            else:
                messages.success(request, 'You are successfully Logged In.')
                return redirect("home")
        else:
            messages.warning(request, 'Invalid Credentials.')

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            myuser = User.objects.create_user(name, email, password)
            myuser.save()

            messages.success(request, 'You are successfully Registered...')
            return redirect("login")
        else:
            messages.warning(request, 'Password is not same. Please check It.')
        
    return render(request, "register.html")


def userlogout(request):
    logout(request)
    messages.success(request, 'You are successfully Logged Out...')
    return redirect("home")
