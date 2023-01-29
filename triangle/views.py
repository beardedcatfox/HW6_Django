from django.shortcuts import render

from triangle.forms import TriangleForm


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
