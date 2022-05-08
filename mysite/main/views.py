from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.utils.translation import gettext_lazy as _


# Create your views here.
# response is to see if it's post or get, it's get by default

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        # saving the check button
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                # validate
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {"ls": ls})  # return view page for their lists


# def home(response):
#   return render(response, "main/home.html", {})


def home(request):
    return render(request, 'main/home.html', {})


def products(request):
    return render(request, 'main/products.html', {})


def register(request):
    return render(request, 'main/register.html', {})


def create(response):
    if response.method == "POST":
        # POST holds information from form
        # this one has a dictionary of all the ID's of different attributes and inputs
        form = CreateNewList(response.POST)

        # is_valid method exists since it inherits from forms.form, which auto checks all defined fields for valid input
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            # User specific save
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)

    else:
        # creates blank new form
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def view(response):
    return render(response, "main/view.html", {})


def testlang(request):
    return HttpResponse(_('Welcome to language translation!'))
