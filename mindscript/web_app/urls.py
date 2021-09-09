
from django.urls import path
from .views import *
from django.http import HttpResponse
from django.conf.urls import url
#Create your views here.


urlpatterns = [
    path('', home,name='home'),
    path('index/', index,name='index'),
    path('about/', about,name='about'),
    path('dashboard/', dashboard,name='dashboard'),
    path('contact/', contact,name='contact'),
    

    path('dashboard/Floor', display_Floor, name="display_Floor"),
    path('dashboard/Concrete', display_Concrete, name="display_Concrete"),
    path('dashboard/Insulation', display_Insulation, name="display_Insulation"),
    path('dashboard/Electrical_wiring', display_Electrical_wiring, name="display_Electrical_wiring"),
    path('dashboard/Cement', display_Cement, name="display_Cement"),
    path('dashboard/Plaster', display_Plaster, name="display_Plaster"),
    path('dashboard/Ceiling', display_Ceiling, name="display_Ceiling"),
    path('dashboard/Paint', display_Paint, name="display_Paint"),
    path('dashboard/Fire_suppression_equip', display_Fire_suppression_equip, name="display_Fire_suppression_equip"),
    path('dashboard/HVAC', display_HVAC, name="display_HVAC"),
    path('dashboard/Masonry', display_Masonry, name="display_Masonry"),
    path('dashboard/Plastic', display_Plastic, name="display_Plastic"),
    path('dashboard/Plumbing', display_Plumbing, name="display_Plumbing"),

    
    url('dashboard/add_Floor', add_Floor, name="add_Floor"),
    url('dashboard/add_Concrete', add_Concrete, name="add_Concrete"),
    url('dashboard/add_Insulation', add_Insulation, name="add_Insulation"),
    url('dashboard/add_Electrical_wiring', add_Electrical_wiring, name="add_Electrical_wiring"),
    url('dashboard/add_Cement', add_Cement, name="add_Cement"),
    url('dashboard/add_Plaster', add_Plaster, name="add_Plaster"),
    url('dashboard/add_Ceiling', add_Ceiling, name="add_Ceiling"),
    url('dashboard/add_Paint', add_Paint, name="add_Paint"),
    url('dashboard/add_Fire_suppression_equip', add_Fire_suppression_equip, name="add_Fire_suppression_equip"),
    url('dashboard/add_HVAC', add_HVAC, name="add_HVAC"),
    url('dashboard/add_Masonry', add_Masonry, name="add_Masonry"),
    url('dashboard/add_Plastic', add_Plastic, name="add_Plastic"),
    url('dashboard/add_Plumbing', add_Plumbing, name="add_Plumbing"),
    
    url(r'^Floor/edit_item/(?P<pk>\d+)$', edit_Floor, name="edit_Floor"),
    url(r'^Concrete/edit_item/(?P<pk>\d+)$', edit_Concrete, name="edit_Concrete"),
    url(r'^Insulation/edit_item/(?P<pk>\d+)$', edit_Insulation, name="edit_Insulation"),
    url(r'^Electrical_wiring/edit_item/(?P<pk>\d+)$', edit_Electrical_wiring, name="edit_Electrical_wiring"),
    url(r'^Cement/edit_item/(?P<pk>\d+)$', edit_Cement, name="edit_Cement"),
    url(r'^Plaster/edit_item/(?P<pk>\d+)$', edit_Plaster, name="edit_Plaster"),
    url(r'^Ceiling/edit_item/(?P<pk>\d+)$', edit_Ceiling, name="edit_Ceiling"),
    url(r'^Paint/edit_item/(?P<pk>\d+)$', edit_Paint, name="edit_Paint"),
    url(r'^Fire_suppression_equip/edit_item/(?P<pk>\d+)$', edit_Fire_suppression_equip, name="edit_Fire_suppression_equip"),
    url(r'^HVAC/edit_item/(?P<pk>\d+)$', edit_HVAC, name="edit_HVAC"),
    url(r'^Masonry/edit_item/(?P<pk>\d+)$', edit_Masonry, name="edit_Masonry"),
    url(r'^Plastic/edit_item/(?P<pk>\d+)$', edit_Plastic, name="edit_Plastic"),
    url(r'^Plumbing/edit_item/(?P<pk>\d+)$', edit_Plumbing, name="edit_Plumbing"),
    

    url(r'^Floor/delete/(?P<pk>\d+)$', delete_Floor, name="delete_Floor"),
    url(r'^Concrete/delete/(?P<pk>\d+)$', delete_Concrete, name="delete_Concrete"),
    url(r'^Insulation/delete/(?P<pk>\d+)$', delete_Insulation, name="delete_Insulation"),
    url(r'^Electrical_wiring/delete/(?P<pk>\d+)$', delete_Electrical_wiring, name="delete_Electrical_wiring"),
    url(r'^Cement/delete/(?P<pk>\d+)$', delete_Cement, name="delete_Cement"),
    url(r'^Plaster/delete/(?P<pk>\d+)$', delete_Plaster, name="delete_Plaster"),
    url(r'^Ceiling/delete/(?P<pk>\d+)$', delete_Ceiling, name="delete_Ceiling"),
    url(r'^Paint/delete/(?P<pk>\d+)$', delete_Paint, name="delete_Paint"),
    url(r'^Fire_suppression_equip/delete/(?P<pk>\d+)$', delete_Fire_suppression_equip, name="delete_Fire_suppression_equip"),
    url(r'^HVAC/delete/(?P<pk>\d+)$', delete_HVAC, name="delete_HVAC"),
    url(r'^Masonry/delete/(?P<pk>\d+)$', delete_Masonry, name="delete_Masonry"),
    url(r'^Plastic/delete/(?P<pk>\d+)$', delete_Plastic, name="delete_Plastic"),
    url(r'^Plumbing/delete/(?P<pk>\d+)$', delete_Plumbing, name="delete_Plumbing"),

    ]
