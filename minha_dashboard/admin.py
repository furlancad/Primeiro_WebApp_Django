from django.contrib import admin
from .models import Produto, Vendedor, Vendas

admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Vendas)
