from django.urls import path

from triangle.views import get_form, person_create, person_update


app_name = 'triangle'
urlpatterns = [
    path('', get_form, name='triangle'),
    path('person/', person_create, name='person_create'),
    path('person/<int:pk>/', person_update, name='person_update'),
]
