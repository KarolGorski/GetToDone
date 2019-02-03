from django.shortcuts import render, redirect
from .models import ToDo, Category
from django.http import HttpResponse

def manage(request):
    todos = ToDo.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = ToDo(title = title, content = content, created= date, category = Category.objects.get(name=category))
            Todo.save()
            return redirect("/manage")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = ToDo.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "manage.html", {"todos": todos, "categories": categories})

def allByCategories(request):
    todos = ToDo.objects.all()
    categories = Category.objects.all()

    wow = [[cat, [todo]] for cat in categories for todo in todos if todo.category == cat]


def start(request):
    return HttpResponse("Hello Start Panel!")

def currentTask(request):
    return HttpResponse("Hello current Task View!")