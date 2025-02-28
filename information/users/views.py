from django.shortcuts import render, redirect
from .models import Teachers, customUser
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False
            user.save()
            messages.success(request, 'Your account has been created!  Wait for admin approval')
            return redirect('login')
    else:
        form = UserRegisterForm()
        print("else")
    return render(request, 'users/register.html', {'form': form})

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


