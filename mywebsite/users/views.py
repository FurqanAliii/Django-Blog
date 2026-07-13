from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages   
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
       form=UserForm(request.POST)
       if form.is_valid():
        form.save()
        messages.success(request,'Account created Successfully! Now you can login')
        return redirect('login')

        print('user register succesfully')
    else:
       form=UserForm()
    return render(request,'users/register.html',{'form':form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect("blog-home")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, 
                                request.FILES,
                                instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request,'Account Updated Successfully')
        return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
           }
    return render(request, 'users/profile.html',context)


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')