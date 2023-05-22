import os

from django.shortcuts import render

def index(request):
    return render(request, os.fspath("mediator/objects/templates/index.html"))


