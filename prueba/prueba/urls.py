from django.contrib import admin
from django.urls import path
from django.conf import settings
from inicio import views
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.principal, name='principal'),
    path('nombre/', views.nombre, name='nombre'),
    path('formulario/', views.formulario, name='formulario'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('consultas/', views.consultas, name='consultas'),

    path('contacto/', views_registros.contacto, name='contacto'),
    path('registrar/', views_registros.registrar, name='registrar'),
    path('consultarComentario/', views_registros.consultarComentario, name='consultarComentario'),
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual,name='ConsultaIndividual' ),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto, name='Editar'),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('consultar1/', views.consultar1, name='consultar1'),


    path('consultar2/', views.consultar2, name='consultar2'),
    path('consultar3/', views.consultar3, name='consultar3'),
    path('consultar4/', views.consultar4, name='consultar4'),
    path('consultar4_1/', views.consultar4_1, name='consultar4_1'),
    path('consultar4_1/sql/', views.consultar4_1_sql, name='consultar4_1_sql'),
    path('consultaORM/', views.consultaORM, name='consultaORM'),
    path('consultasSQL/', views.consultasSQL, name='consultasSQL'),
    path('consultar5/', views.consultar5, name='consultar5'),
    path('consultar5/sql/', views.consultar5_sql, name='consultar5_sql'),
    path('consultar6/', views.consultar6, name='consultar6'),
    path('consultar6/sql/', views.consultar6_sql, name='consultar6_sql'),
    path('consultar7/', views.consultar7, name='consultar7'),
    path('consultar7/sql/', views.consultar7_sql, name='consultar7_sql'),

    path('comentarios/fechas/', views_registros.comentariosFechas, name='comentariosFechas'),
    path('comentarios/busqueda/', views_registros.buscarComentario, name='buscarComentario'),
    path('comentarios/usuario/', views_registros.comentariosUsuario, name='comentariosUsuario'),
    path('comentarios/expresion1/', views_registros.consultaExpresion1, name='consultaExpresion1'),
    path('comentarios/expresion2/', views_registros.consultaExpresion2, name='consultaExpresion2'),


    path('comentarios/fechas/sql/', views_registros.comentariosFechas_sql, name='comentariosFechas_sql'),
    path('comentarios/busqueda/sql/', views_registros.buscarComentario_sql, name='buscarComentario_sql'),
    path('comentarios/usuario/sql/', views_registros.comentariosUsuario_sql, name='comentariosUsuario_sql'),
    path('comentarios/expresion1/sql/', views_registros.consultaExpresion1_sql, name='consultaExpresion1_sql'),
    path('comentarios/expresion2/sql/', views_registros.consultaExpresion2_sql, name='consultaExpresion2_sql'),

    path('Subir/', views_registros.subir_archivo, name='Subir'),



]


