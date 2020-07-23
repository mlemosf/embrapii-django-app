from django.shortcuts import render
from rest_framework import generics
from .models import Register
from .forms import PostRegister
#from .serializers import RegisterSerializer
from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    print(request.method)
    if request.method == 'DELETE':
        print(request.DELETE)
    # return render(request, 'registro/home.html')

# Novo registro
@csrf_exempt
def newregister(request):
    if request.method == 'POST':
        register = Register()
        register.name = request.POST.get('name')
        register.birthdate = request.POST.get('birthdate')
        register.testtype = request.POST.get('testtype')
        register.testresult = request.POST.get('testresult')
        register.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registro/newregister.html')
    #return render(request, 'registro/newregister.html',{ 'form': register })


