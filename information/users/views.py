from django.shortcuts import render, redirect
from .models import Teachers
from django.contrib import messages

# Create your views here.


def dashboard(request):

 return render(request, 'users/dashboard.html')




def homePage(request):

    
    return render(request, 'users/homepage.html')




def Teacher_login(request):
    print("login")
    if request.method == "POST":
        print("post")
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        print("Username = ", username)
        print("Pass = ", password)
        try:
            print("try")
            teacher = Teachers.objects.get(Username=username)
            print("Teacher = ", teacher)
            if teacher.check_password(password):
                print("if")
                #request.session['user_id '] = teacher.id
                #login(request, teacher)
                return redirect('Dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        except:
            print("except")
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')


