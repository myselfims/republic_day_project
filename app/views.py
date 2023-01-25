from django.shortcuts import render
from django.shortcuts import redirect
from .models import User,Visit

# Create your views here.

def home(request):
    
    return redirect('create')


def wish(request, name):
    visit = Visit.objects.get(id=1)
    visit.count = visit.count + 1
    visit.save()
    link= str(request.build_absolute_uri()).replace('wish','wish2')
    print(link)
    print('11')
    return render(request,'base.html',{'link':link})

def wish2(request,name):
    print(name)
    return render(request,'wish.html',{'name':name})


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = User(name=name)
        model.save()
        name = str(name).replace(' ','_')
        link = str(request.build_absolute_uri()).replace('create','wish')+name
        print(link)
        return render(request, 'create.html',{'created':True,'link':link})
    return render(request,'create.html')
