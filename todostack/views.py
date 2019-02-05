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
            estimatedTime = parseTime(request.POST["workingTime"])
            content = title + " -- " + date + " " + category
            Todo = ToDo(title = title,
                        content = content,
                        created= date,
                        category = Category.objects.get(name=category),
                        difficulty = Difficulty.objects.get(name=difficulty),
                        priority = Priority.objects.get(name=priority),
                        estimatedTime=estimatedTime)
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

    if "manage" in request.GET:
        return redirect('/manage')

    if request.method == "POST":
        if "startApp" in request.POST:
            workingTime = request.POST["workingTime"]
            request.session['workingTime'] = parseTime(workingTime)
            return redirect('/work')

    return render(request, "start.html", {"categories": categories,
                                          "difficulties": difficulties,
                                          "priorities": priorities})

import operator
def work(request):
    todoss = ToDo.objects.all()
    if(len(todoss)==0):
        return redirect('/start')
    todoss = sorted(todoss, key=lambda todo: todo.estimatedTime)
    time = 0
    todos =[]
    for todo in todoss:
        time+=todo.estimatedTime
        if time<=request.session['workingTime']:
            todos.append(todo)
        else:
            break

    todo=todos[0]
    todos = todos[1:len(todos)]

    if request.method == "POST":
        if "taskFinish" in request.POST:
            workedTime = request.POST['workingTime']
            Difficulty.objects.get(id=todo.difficulty.id).current_multiplier \
                += (parseTime(workedTime)-todo.estimatedTime)/2

            ToDo.objects.filter(id=todo.id).delete()
            return redirect('/work')



    return render(request,"work.html", {"firstTodo":todo,
                                        "todos": todos})



def parseTime(text):
    text.replace(" ","")
    tab = text.split(',')
    if len(tab)>1:
        return int(tab[0])*60 + int(tab[1])
    if len(tab) ==1:
        return int(tab[0])*60

def parseToTime(num):
    minutes = num%60
    hours = num/60
    return str(hours)+","+str(minutes)



 #wow = [(cat, [todo]) for cat in categories for todo in todos if todo.category == cat]
