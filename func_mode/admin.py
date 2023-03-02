from django.contrib import admin
from .models import Pedido, Status

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','cliente','data','status', 'pago']
    list_display_links = ['id','cliente']
    list_editable = ['status']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['status']
    list_display_links = ['status']

admin.site.register(Status, StatusAdmin)
admin.site.register(Pedido,PedidoAdmin)
# Register your models here.
