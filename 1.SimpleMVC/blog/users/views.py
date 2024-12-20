from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from . import forms

# Create your views here.
def register_view(request):
    if request.method != 'POST':
        form = forms.CustomUserForm()
    else:
        form = forms.CustomUserForm(request.POST)
        print("is valid "+str(form.is_valid()))
        print("form "+str(form))
        if form.is_valid():
            #form.save()
            login(request, form.save())
            return redirect('posts:list')
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")