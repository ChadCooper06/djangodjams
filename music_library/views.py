from django.shortcuts import render

from django.http import JsonResponse
from .models import *


def individual_song(request, id):
    s = Songs.objects.filter(id=id).values()
    data = list(s)
    return JsonResponse(data[0])

#fn to return JSON
#query the DB
#turn that query into a list
#get the values you need only
#send that data to the frontend
