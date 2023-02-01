from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from triangle.forms import PersonForm, TriangleForm

from .models import Person


def get_form(request):
    hipotenuse = None
    if request.method == 'GET':
        form = TriangleForm(request.GET)
        if form.is_valid():
            catet1 = form.cleaned_data['legA']
            catet2 = form.cleaned_data['legB']
            hipotenuse = round(((catet1 ** 2 + catet2 ** 2) ** 0.5), 3)
    else:
        form = TriangleForm()
    return render(request,
                  'triangle/triangle.html',
                  {'form': form,
                   'hipotenuse': hipotenuse})


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Congratulations!</h2><p>Person was created successfully</p>')
    else:
        form = PersonForm()
    return render(request, 'triangle/create_person.html', {'form': form})


def person_update(request, pk):
    person = get_object_or_404(Person, id=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Congratulations!</h2><p>Person was updated successfully</p>')
    else:
        form = PersonForm(instance=person)
    return render(request, 'triangle/update_person.html', {'form': form})
