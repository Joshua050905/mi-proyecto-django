from django.contrib import admin
from django.urls import path
from django.conf import settings
from inicio import views
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),  # Dejé solo una ruta ''
    path('nombre/', views.nombre, name='nombre'),
    path('contacto/', views_registros.contacto, name='contacto'),  # minúsculas
    path('formulario/', views.formulario, name='formulario'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('registrar/', views_registros.registrar, name='registrar'),  # <-- AQUÍ FALTABA LA COMA
    path('editarComentario/<int:id>/', views_registros.editarComentario, name='editarComentario'), # <-- Agregada por buena práctica
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentario, name='eliminarComentario'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)