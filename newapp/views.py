from django.shortcuts import redirect, render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['name']
    y=request.POST['email']
    z=request.POST['Department']
    m=request.POST['dateofjoining']
    mem=Member(name=x,Email=y,dept=z,dof=m)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['email']
    z=request.POST['Department']
    m=request.POST['dateofjoining']
    mem=Member.objects.get(id=id)
    mem.name=x
    mem.Email=y
    mem.dept=z
    mem.dof=m
    mem.save()
    return redirect("/")
