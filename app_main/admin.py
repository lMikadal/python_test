from django.contrib import admin
from .models import Good

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'stock']

admin.site.register(Good, GoodAdmin)
