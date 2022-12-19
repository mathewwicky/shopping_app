from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
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

