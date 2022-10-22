from django.contrib import admin
from.models import Endereco,Account

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['conta','estado', 'cidade']
    list_display_links = ['conta']
    search_fields = ['conta','estado','cidade']

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['user','nome','telefone','admin']
    list_display_links = ['user', 'nome']
    list_editable = ['telefone', 'admin']
    search_fields = ['user', 'nome','telefone','admin']

admin.site.register(Endereco,EnderecoAdmin)
admin.site.register(Account,AccountsAdmin)

# Register your models here.
