from django.http import HttpResponse
import pdb

def hello(request):

	return HttpResponse('Hola, world')
