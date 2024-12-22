# transport/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegistrationForm, ProfileForm, OrderForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Order

def home(request):
    return render(request, 'transport/home.html')

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)  # Log the user in after registration
            return redirect('home')  # Replace 'home' with your homepage URL name
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Assign the current user to the order
            order.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'transport/create_order.html', {'form': form})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'transport/order_detail.html', {'order': order})