from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html',{"success":'Registration Successful please login'})
        else:
            error_message = form.errors.as_text()
            return render(request,'register.html',{"error":error_message})
    context = {'form':form}
    return render(request,'register.html',context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':"Invalid credentials please tyr again"})
    return render(request,'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")