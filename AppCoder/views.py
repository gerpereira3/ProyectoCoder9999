from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Fede"
    }
    return render(request, "AppCoder/cursos.html", contexto)


def crear_curso(request):
    curso = Curso(nombre ="Python", camada=41000)
    curso.save()

    contexto = {"curso": curso}

    return redirect("/app/cursos/") # get
    #return render(request, 'index.html', contexto)
    #return HttpResponse(f"Su curso es {curso.nombre} y la camada es {curso.camada}")

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fede"}
    return render(request, 'index.html', contexto)


