# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

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
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )