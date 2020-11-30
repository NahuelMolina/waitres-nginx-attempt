from django.http import HttpResponse
import pdb

def hello(request):
    return HttpResponse('Hola, world')

def houses_views(request):
    return HttpResponse('views of houses')
