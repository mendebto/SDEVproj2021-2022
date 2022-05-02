from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# creating a database model called to do list
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    # when creating attribute, create as a class variable and
    # give type of field wanting to be stored in database
    name = models.CharField(max_length=200)

    # define a method to print out name
    def __str__(self):
        return self.name


class Item(models.Model):
    # related to ToDoList
    # doesn't know the type so ToDoList has to be defined as foreign key
    # also on_delete means if ToDoList is deleted this deletes too in a cascade way
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # CharField is just a string
    text = models.CharField(max_length=300)

    # Will tell us if the to do item is completed
    complete = models.BooleanField()

    def __str__(self):
        return self.text
