from django.contrib import admin

from .models import Genero, Livro, CopiaLivro, Autor


class AutorAdmin(admin.ModelAdmin):
    list_display = ('sobrenome', 'nome', 'data_de_nascimento', 'data_de_falecimento')
    fields = ['nome', 'sobrenome', ('data_de_nascimento', 'data_de_falecimento')]


class CopiaLivroAdmin(admin.ModelAdmin):
    list_filter = ('status', 'devolucao')


class CopiaLivroInline(admin.TabularInline):
    model = CopiaLivro


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'mostrar_genero')

    inlines = [CopiaLivroInline]


admin.site.register(Genero)
admin.site.register(Livro, LivroAdmin)
admin.site.register(CopiaLivro, CopiaLivroAdmin)
admin.site.register(Autor, AutorAdmin)
