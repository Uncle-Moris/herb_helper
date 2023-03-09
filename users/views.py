from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = UserRegisterForm()
	return render(request=request, template_name="users/register.html", context={"form":form})

# class UserRegisterView(CreateView):
#     template_name = "users/register.html"
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('register')
