from django.contrib import admin
from .models import Filme, Episodios, usuarios
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields':('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodios)
admin.site.register(usuarios, UserAdmin)


# Register your models here.
