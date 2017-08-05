# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book

# Create your views here.

def read(request, id):
    book = Book.objects.get(id=id).to_user()
    return HttpResponse(book.title)

# def index(request):
#     return Book.objects.
