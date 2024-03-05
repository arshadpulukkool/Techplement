from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import History

def home(request):
    return render(request, 'home.html')

def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/operation')
        else:
            messages.error(request, 'Invalid Credentials , Create an account')
            print("error")
            return redirect('/login')
    else:
       return render(request, 'home.html')

def register(request,):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                print("Username already registered")
                return redirect('/login')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username, password=password1)
                user.save()
                print("user created")
                return redirect('/login')
        else:
            messages.info(request, 'Password does not match')
            print("Password is not matching")
        return redirect('/reg')

    else:
        return render(request, 'home.html')

@login_required()
def operations(request):
    if request.method == 'POST':
        number1 = request.POST['fnum']
        number2 = request.POST['snum']
        operation = request.POST['operator']
        if operation == "add":
            result = float(number1) + float(number2)
            data = History(value1=number1,operation=operation,value2=number2,result=result,user=request.user)
            data.save()
        elif operation == "sub":
            result = float(number1) - float(number2)
            data = History(value1=number1, operation=operation, value2=number2, result=result,user=request.user)
            data.save()
        elif operation == "mul":
            result = float(number1) * float(number2)
            data = History(value1=number1, operation=operation, value2=number2, result=result,user=request.user)
            data.save()
        elif operation == "div":
            result = float(number1) / float(number2)
            data = History(value1=number1, operation=operation, value2=number2, result=result,user=request.user)
            data.save()
        datas = History.objects.filter(user=request.user)
        return render(request, 'operations.html',{'result':result,'datas':datas})

    else:
        datas = History.objects.filter(user=request.user)
        return render(request, 'operations.html',{'datas':datas})


#AnonymousUSer function is used for doing calculation for non-logged users. Not providing history
def AnonymousUser(request):
    if request.method == 'POST':
        number1 = request.POST['fnum']
        number2 = request.POST['snum']
        operation = request.POST['operator']
        if operation == "add":
            result = float(number1) + float(number2)

        elif operation == "sub":
            result = float(number1) - float(number2)

        elif operation == "mul":
            result = float(number1) * float(number2)

        elif operation == "div":
            result = float(number1) / float(number2)

        return render(request, 'NotLoggedUser.html',{'result':result})

    else:
        return render(request, 'NotLoggedUser.html')


#Here delete function is used for deleting history OneByOne for seperate users using their id.
def delete(request, id):
    hs = History.objects.get(id=id)
    hs.delete()
    return redirect('/operation')

def logout_view(request):
    logout(request)
    return redirect('/')


