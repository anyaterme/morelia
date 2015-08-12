from django.shortcuts import render

from django.views.generic import CreateView

from .forms import MyModelForm
from .models import MyModel


class MyCreateView(CreateView):
    form_class = MyModelForm
    model = MyModel

# Create your views here.
