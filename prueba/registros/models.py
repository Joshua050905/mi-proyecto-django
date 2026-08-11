from django.db import models
from ckeditor.fields import RichTextField

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12, verbose_name='Matrícula')  # Sin unique por ahora
    nombre = models.CharField(max_length=100) 
    carrera = models.CharField(max_length=100)
    turno = models.CharField(max_length=10, choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino')])
    imagen = models.ImageField(upload_to="alumnos/", null=True, blank=True, verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['-created']

    def __str__(self):
        return f"{self.matricula} - {self.nombre}"

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']

    def __str__(self):
        return f"Comentario de {self.alumno.nombre}"

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje[:50]
    

class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100)
    descripcion = models.FileField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre