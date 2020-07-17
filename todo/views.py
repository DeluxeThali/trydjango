from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todoitem

def todoview(request):
    all_items = todoitem.objects.all()
    return render(request,'todo.html',
                  {'all_todo' : all_items})

def addtodo(request):
    c = request.POST['Content']
    new_item  = todoitem(content = c)
    new_item.save()
    return HttpResponseRedirect('/')

def deletetodo(request, todo_id):
    del_item = todoitem.objects.get(id=todo_id)
    del_item.delete()
    return HttpResponseRedirect('/')



# Create your views here.
