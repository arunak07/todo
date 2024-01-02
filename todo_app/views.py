from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
no = 0
def home(request):
    global no
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        no = no + 1
        data = Todo(no=abs(no),title=title,description=description)
        data.save()
        return redirect('home')

    data1 = Todo.objects.all()
    return render(request,'index.html',{'val': data1})
    

def update(request,no):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        data = Todo.objects.get(no=no)
        data.title=title
        data.description=description
        data.save()
        return redirect('home')
    todo = Todo.objects.filter(no = no).first()
    return render(request,'update.html',{'todo':todo})

def delete(request,no):
    todo = Todo.objects.filter(no = no).first()
    todo.delete()
    def dec():
        global no
        no = no - 1
    dec()
    return redirect('home')