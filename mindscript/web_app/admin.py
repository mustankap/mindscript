# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(
    

 Floor,
 Concrete,
 Insulation,
 Electrical_wiring,
 Cement,
 Plaster,
 Ceiling,
 Paint,
 Fire_suppression_equip,
 HVAC,
 Masonry,
 Plastic,
 Plumbing,
)
class ViewAdmin(admin.ModelAdmin):
    exclude = ('id', )