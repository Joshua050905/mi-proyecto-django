from django.shortcuts import render, HttpResponse
from registros.models import Alumnos
import datetime

# Create your views here.



def principal(request):
    alumnos = Alumnos.objects.all()
    return render(request, "inicio/principal.html", {'alumnos': alumnos})

def nombre(request):
    return render(request, "inicio/nombre.html")

def contacto(request):
    return render(request ,"inicio/contacto.html" )
   

def formulario(request):
    
    return render(request , "inicio/formulario.html")


def ejemplo(request):
    return render(request , "inicio/ejemplo.html")

def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno","imagen")
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(nombre__startswith='A')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar4_1(request):
    alumnos = Alumnos.objects.filter(turno='Vespertino')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar4_1_sql(request):
    alumnos = Alumnos.objects.raw(
        "SELECT * FROM registros_alumnos WHERE turno = %s ORDER BY nombre",
        ['Vespertino']
    )
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultaORM(request):
    alumnos = Alumnos.objects.filter(
        carrera="TI"
    ).order_by('-turno')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultasSQL(request):
    alumnos = Alumnos.objects.raw("""
        SELECT id, matricula, nombre,
               carrera, turno, imagen
        FROM registros_alumnos
        WHERE carrera='TI'
        ORDER BY turno DESC
    """)
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__in=['JUAN', 'ANA'])
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar5_sql(request):
    alumnos = Alumnos.objects.raw(
        "SELECT * FROM registros_alumnos WHERE UPPER(nombre) IN (%s, %s)",
        ['JUAN', 'ANA']
    )
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar6(request):
    fechaInicio = datetime.date(2026, 8, 3)
    fechaFin = datetime.date(2026, 8, 4)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar6_sql(request):
    fechaInicio = datetime.date(2026, 8, 3)
    fechaFin = datetime.date(2026, 8, 4)
    alumnos = Alumnos.objects.raw(
        "SELECT * FROM registros_alumnos WHERE created BETWEEN %s AND %s",
        [fechaInicio, fechaFin]
    )
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar7(request):
    # El comentario que existe actualmente en la base de datos contiene "gracias".
    alumnos = Alumnos.objects.filter(comentario__coment__contains='gracias')
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})


def consultar7_sql(request):
    alumnos = Alumnos.objects.raw(
        "SELECT DISTINCT a.* FROM registros_alumnos a "
        "JOIN registros_comentario c ON c.alumno_id = a.id "
        "WHERE c.coment LIKE %s",
        ['%gracias%']
    )
    return render(request , "inicio/consultas.html", {'alumnos': alumnos})
