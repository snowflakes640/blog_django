from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account Created. Ready to Login?")
            return redirect("login")
        # else:
        #     print("Form is not valid.")
        #     print(form.errors)

    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required   
def profile(request):
    return render(request, "users/profile.html")


# def register(request):
#     messages.success(request, "This is a success message!")
#     messages.error(request, "This is an error message!")
#     return render(request, "users/register.html")