import os

from django.shortcuts import render
from sftp_machine import connection_agent as sftpDoer
# from mediator import objects as objs
import mediator as md
# Most (maybe all) of the views wil involve interaction with SFTP_machine, which instantiates an
# object to make connections and send SFTP commands. As of now every request will create and destroy
# a new instance of SFTP_Doer. This is horribly inefficient so...
# TODO: Implement caching or sessions to persist SFTP_Doer instances


def index(request):

    return render(request, os.fspath("index.html"), content_type="text/html")


def books_indx(request):
    return render(request, os.fspath("books.html"), content_type="text/html")
