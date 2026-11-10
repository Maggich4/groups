from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .forms import RegisterForm, RegisterFormJKArman

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            return redirect('register')
        
    else:
        form = RegisterForm()
        
    return render(request, 'permision/register.html', {
        "form": form
    })


def register_JKArman(request):
    if request.method == "POST":
        form = RegisterFormJKArman(request.POST)
        
        if form.is_valid():
            user = form.save()
            return redirect('register_JKArman')
        
    else:
        form = RegisterFormJKArman()
        
    return render(request, 'permision/register.html', {
        "form": form
    })

def add_user_to_student_group(user):
    group = Group.objects.get(name='Student')
    
    user.group.add(group)
    
def add_user_to_teacher_group(user):
    group = Group.objects.get(name='Teacher')
    
    user.group.add(group)