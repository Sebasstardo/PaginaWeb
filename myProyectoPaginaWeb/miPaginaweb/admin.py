from django.contrib import admin
from .models import Producto,Insumo,SliderIndex,MisionVision, Galeria
# Register your models here.

class InsumosAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','stock','descripcion','imagen','Producto']
    search_fields=['nombre']
    list_per_page = 10
    list_filter =['Producto']

class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['indet','imagen']
    search_fields=['indet']
    list_per_page =10
    
class MisionVisionAdmin(admin.ModelAdmin):
    list_display=['indet','mision','vision']
    search_fields =['indet']
    list_per_page=10

class GaleriaAdmin(admin.ModelAdmin):
    list_displat = ['ident','imagen']
    search_fields = ['ident']
    list_per_page = 10

admin.site.register(Producto)
admin.site.register(Insumo,InsumosAdmin)
admin.site.register(SliderIndex,SliderIndexAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(MisionVision)


