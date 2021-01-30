from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

tasks = ["Hello"]


class NewTaskForm(forms.Form):
    task = forms.CharField(label="TaskName")


def main(request):

    return render(request, 'main.html', {
        "tasks": tasks
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:main"))
        else:
            return render(request, "addtask.html", {
                "form": form
            })

    return render(request, 'addtask.html', {
        "form": NewTaskForm()
    })
