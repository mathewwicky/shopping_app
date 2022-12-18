from django.shortcuts import render,redirect
from .forms import UserForm
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
