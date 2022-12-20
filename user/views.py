from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
           user = form.save()
           return redirect('myapp/products')


    form = UserForm()
    context = {
        'form':form,
    }

    return render(request,'user/register.html',context)
    
@login_required
def profile(request):
    return render(request,'user/profile.html')

def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user, image=image, contact_number=contact_number )
        profile.save()
    return render(request,'user/create_profile.html')

