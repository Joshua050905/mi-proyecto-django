from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos, ComentarioContacto 
from .forms import ComentarioContactoForm

# Create your views here.

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            comentarios = ComentarioContacto.objects.all() 
            return render(request, "registros/editarContacto.html", {'comentarios': comentarios})
    else:
        form = ComentarioContactoForm()
    
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/contacto.html", {'form': form, 'comentarios': comentarios})

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})

# ==========================================
#  VISTAS DE EDICIÓN Y ELIMINACIÓN
# ==========================================

def editarComentario(request, id):
    # Recupera el comentario por su ID o muestra error 404 si no existe
    comentario = get_object_or_404(ComentarioContacto, id=id)
    
    if request.method == 'POST':
        # instance=comentario le dice a Django que edite este registro en lugar de crear uno nuevo
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('registrar')  # Redirige a la lista tras guardar
    else:
        # Carga el formulario con los datos actuales del comentario
        form = ComentarioContactoForm(instance=comentario)
        
    return render(request, "registros/editarContacto.html", {'form': form, 'comentario': comentario})

def eliminarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    comentario.delete()  # Borra el registro de la base de datos
    return redirect('registrar')  # Redirige de vuelta a la lista