from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from datetime import date
from django.db.models import Q
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


def ejecutar_sql(sql, params=None):
    with connection.cursor() as c:
        c.execute(sql, params or [])
        columns = [col[0] for col in c.description]
        return [dict(zip(columns, row)) for row in c.fetchall()]


# Create your views here.

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})


def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {"form": form})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultarComentario')
    else:
        form = ComentarioContactoForm()

    return render(request, "registros/contacto.html", {'form': form})


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(
        request,
        "registros/editarContacto.html",
        {"comentarios": comentarios}
    )


def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(instance=comentario)

    return render(
        request,
        "registros/editarComentario.html",
        {
            "form": form,
            "comentario": comentario
        }
    )


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('consultarComentario')
    else:
        form = ComentarioContactoForm(instance=comentario)

    return render(
        request,
        "registros/editarComentario.html",
        {
            "form": form,
            "comentario": comentario
        }
    )


def eliminarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == 'POST':
        comentario.delete()
        return redirect('consultarComentario')

    return render(
        request,
        "registros/ConfirmarEliminacion.html",
        {
            "comentario": comentario
        }
    )


def comentariosFechas(request):
    comentarios = ComentarioContacto.objects.filter(
        created__date__range=(date(2026, 6, 20), date(2026, 8, 4))
    )
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


def comentariosFechas_sql(request):
    sql = """
    SELECT id, usuario, mensaje, created
    FROM registros_comentariocontacto
    WHERE DATE(created) BETWEEN %s AND %s
    ORDER BY created DESC
    """
    comentarios = ejecutar_sql(sql, ['2026-06-20', '2026-08-04'])
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


def buscarComentario(request):
    comentarios = ComentarioContacto.objects.filter(
        mensaje__icontains="gracias"
    )
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})
def buscarComentario_sql(request):
    sql = """
    SELECT id, usuario, mensaje, created
    FROM registros_comentariocontacto
    WHERE mensaje LIKE %s
    ORDER BY created DESC
    """
    comentarios = ejecutar_sql(sql, ['%gracias%'])
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


# Comentarios de un usuario
def comentariosUsuario(request):
    comentarios = ComentarioContacto.objects.filter(
        usuario="Admin"
    )
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})
def comentariosUsuario_sql(request):
    sql = """
    SELECT id, usuario, mensaje, created
    FROM registros_comentariocontacto
    WHERE usuario = %s
    ORDER BY created DESC
    """
    comentarios = ejecutar_sql(sql, ['Admin'])
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


# Consulta con expresión (Q)
def consultaExpresion1(request):
    comentarios = ComentarioContacto.objects.filter(
        Q(mensaje__icontains="gracias") | Q(mensaje__icontains="excelente")
    )
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


def consultaExpresion1_sql(request):
    sql = """
    SELECT id, usuario, mensaje, created
    FROM registros_comentariocontacto
    WHERE mensaje LIKE %s OR mensaje LIKE %s
    ORDER BY created DESC
    """
    comentarios = ejecutar_sql(sql, ['%gracias%', '%excelente%'])
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


# Segunda consulta con expresión (Q)
def consultaExpresion2(request):
    comentarios = ComentarioContacto.objects.filter(
        ~Q(mensaje__icontains="malo")
    )
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


def consultaExpresion2_sql(request):
    sql = """
    SELECT id, usuario, mensaje, created
    FROM registros_comentariocontacto
    WHERE mensaje NOT LIKE %s
    ORDER BY created DESC
    """
    comentarios = ejecutar_sql(sql, ['%malo%'])
    return render(request, "registros/editarContacto.html", {"comentarios": comentarios})


def subir_archivo(request):
    return archivos(request)


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else :
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html",{'archivo' : Archivos})