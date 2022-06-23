from django.shortcuts import render

# Create your views here.
def feriado(request):
    return render( request, "teste.html")