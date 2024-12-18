from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            login(request, form.save())
            return redirect('posts:list')
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")