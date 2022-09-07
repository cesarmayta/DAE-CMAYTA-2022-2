from django.shortcuts import render


from .models import Pregunta,Opcion

# Create your views here.
def index(request):
    lista_preguntas = Pregunta.objects.all()
    #select * from encuesta_pregunta
    print(lista_preguntas)

    context = {
        'preguntas':lista_preguntas
    }

    return render(request,'encuesta/index.html',context)