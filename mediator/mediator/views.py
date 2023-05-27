import os

from django.shortcuts import render


# Most (maybe all) of the views will involve interaction with SFTP_machine, which instantiates an
# object to make connections and send SFTP commands. As of now every request will create and destroy
# a new instance of SFTP_Doer. This is horribly inefficient so...
# TODO: Implement caching or sessions to persist SFTP_Doer instances


def index(request):
    return render(request, os.fspath("mediator/objects/templates/index.html"))


def media_root(request):
    pass