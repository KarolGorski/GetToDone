from django.shortcuts import render, redirect
from .models import ToDo, Category, Difficulty, Priority
from django.http import HttpResponse

def manage(request):
    todos = ToDo.objects.all()
    categories = Category.objects.all()
    difficulties = Difficulty.objects.all()
    priorities = Priority.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            difficulty = request.POST["difficulty_select"]
            priority = request.POST["priority_select"]
            content = title + " -- " + date + " " + category
            Todo = ToDo(title = title,
                        content = content,
                        created= date,
                        category = Category.objects.get(name=category),
                        difficulty = Difficulty.objects.get(name=difficulty),
                        priority = Priority.objects.get(name=priority))
            Todo.save()
            return redirect("/manage")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = ToDo.objects.get(id=int(todo_id))
                todo.delete()

        if "startApp" in request.GET:
            return redirect('/start')

    return render(request, "manage.html", {"todos": todos,
                                           "categories": categories,
                                           "difficulties" : difficulties,
                                           "priorities" : priorities})


def start(request):
    todos = ToDo.objects.all()
    categories = Category.objects.all()
    difficulties = Difficulty.objects.all()
    priorities = Priority.objects.all()

    if request.method == "POST":
        if "startApp" in request.POST:
            workingTime = request.POST["workingTime"]
            request.session['selected category'] = request.POST["category_select"]
            request.session['selected difficulty'] = request.POST["difficulty_select"]
            request.session['selected priority'] = request.POST["priority_select"]
            request.session['workingTime'] = parseTime(workingTime)
            return redirect('/work')

    return render(request, "start.html", {"categories": categories,
                                          "difficulties": difficulties,
                                          "priorities": priorities})


def work(request):

    todos = ToDo.objects.all()

    #for todo in todos:

    return render(request,"work.html", {"todos": todos})



def parseTime(text):
    text.replace(" ","")
    tab = text.split(',')
    return int(tab[0])*60 + int(tab[1])



 #wow = [(cat, [todo]) for cat in categories for todo in todos if todo.category == cat]
