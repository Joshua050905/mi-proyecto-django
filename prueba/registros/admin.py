from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

@admin.register(Alumnos)
class AlumnosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    list_per_page = 10
    list_editable = ('nombre', 'carrera', 'turno')
    ordering = ('-created',)  # Orden por defecto
    fieldsets = (('Datos del Alumno', {'fields': ('matricula', 'nombre', 'imagen')}), ('Datos Académicos', {'fields': ('carrera', 'turno')}), ('Fechas', {'fields': ('created', 'updated'), 'classes': ('collapse',)}))
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.username == "pepe":
            return ('created', 'updated', 'matricula', 'nombre', 'carrera', 'turno', 'imagen')
        elif request.user.groups.filter(name="grupo1").exists():
            return ('created', 'updated', 'matricula', 'turno')
        elif request.user.groups.filter(name="dins").exists():
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
        else:
            return ('created', 'updated')
    
    def has_add_permission(self, request):
        # Solo 'pepe' puede agregar
        return request.user.username == "pepe" or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="grupo1").exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if request.user.username == "pepe":
            return False
        return super().has_change_permission(request, obj)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'get_comentario_corto', 'created')
    search_fields = ('id', 'coment', 'alumno__nombre', 'alumno__matricula')
    date_hierarchy = 'created'
    list_filter = ('created', 'alumno__carrera')
    list_per_page = 10
    readonly_fields = ('created',)
    autocomplete_fields = ['alumno']  # Buscador para el ForeignKey si tienes muchos alumnos
    
    def get_comentario_corto(self, obj):
        return obj.coment[:50] + '...' if len(obj.coment) > 50 else obj.coment
    get_comentario_corto.short_description = 'Comentario'

@admin.register(ComentarioContacto)
class ComentarioContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'get_mensaje_corto', 'created')
    search_fields = ('id', 'usuario', 'mensaje')
    date_hierarchy = 'created'
    list_filter = ('created',)
    list_per_page = 10
    readonly_fields = ('created', 'id')
    
    def get_mensaje_corto(self, obj):
        return obj.mensaje[:50] + '...' if len(obj.mensaje) > 50 else obj.mensaje
    get_mensaje_corto.short_description = 'Mensaje'