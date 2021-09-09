from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
# from .forms import *

# Create your views here.
def home(request):
    return render(request,'web_app/base.html')

def about(request):
    return render(request,'web_app/about.html')

def dashboard(request):
    return render(request,'web_app/dashboard.html')

def contact(request):
    return render(request,'web_app/contact.html')

def index(request):
    return render(request,'web_app/index.html')


def display_Floor(request):
    items = Floor.objects.all()
    context = {
        'items': items,
        'header': 'Floors',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Concrete(request):
    items = Concrete.objects.all()
    context = {
        'items': items,
        'header': 'Concrete',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Insulation(request):
    items = Insulation.objects.all()
    context = {
        'items': items,
        'header': 'Insulation',
    }
    return render(request, 'web_app/dashboard.html', context)


def display_Electrical_wiring(request):
    items = Electrical_wiring.objects.all()
    context = {
        'items': items,
        'header': 'Electrical_wiring',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Cement(request):
    items = Cement.objects.all()
    context = {
        'items': items,
        'header': 'Cement',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Plaster(request):
    items = Plaster.objects.all()
    context = {
        'items': items,
        'header': 'Plaster',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Ceiling(request):
    items = Ceiling.objects.all()
    context = {
        'items': items,
        'header': 'Ceiling',
    }
    return render(request, 'web_app/dashboard.html', context)


def display_Paint(request):
    items = Paint.objects.all()
    context = {
        'items': items,
        'header': 'Paint',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Fire_suppression_equip(request):
    items = Fire_suppression_equip.objects.all()
    context = {
        'items': items,
        'header': 'Fire_suppression_equip',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_HVAC(request):
    items = HVAC.objects.all()
    context = {
        'items': items,
        'header': 'HVAC',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Masonry(request):
    items = Masonry.objects.all()
    context = {
        'items': items,
        'header': 'Masonry',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Plastic(request):
    items = Plastic.objects.all()
    context = {
        'items': items,
        'header': 'Plastic',
    }
    return render(request, 'web_app/dashboard.html', context)

def display_Plumbing(request):
    items = Plumbing.objects.all()
    context = {
        'items': items,
        'header': 'Plumbing',
    }
    return render(request, 'web_app/dashboard.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = cls()
        return render(request, 'web_app/add_new.html', {'form' : form})

def add_Floor(request):
    return add_item(request, FloorForm)

def add_Concrete(request):
    return add_item(request, ConcreteForm)

def add_Insulation(request):
    return add_item(request, InsulationForm)

def add_Electrical_wiring(request):
    return add_item(request, Electrical_wiringForm)

def add_Cement(request):
    return add_item(request, CementForm)
def add_Plaster(request):
    return add_item(request,PlasterForm)
def add_Ceiling(request):
    return add_item(request, CeilingForm)
def add_Paint(request):
    return add_item(request, PaintForm)
def add_Fire_suppression_equip(request):
    return add_item(request, Fire_suppression_equipForm)
def add_HVAC(request):
    return add_item(request, HVACForm)
def add_Masonry(request):
    return add_item(request, MasonryForm)
def add_Plastic(request):
    return add_item(request, PlasticForm)
def add_Plumbing(request):
    return add_item(request, PlumbingForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = cls(instance=item)

        return render(request, 'web_app/edit_item.html', {'form': form})

def edit_Floor(request, pk):
    return edit_item(request, pk, Floor, FloorForm)
def edit_Concrete(request, pk):
    return edit_item(request, pk, Concrete, ConcreteForm)
def edit_Insulation(request, pk):
    return edit_item(request, pk, Insulation, InsulationForm)
def edit_Electrical_wiring(request, pk):
    return edit_item(request, pk, Electrical_wiring, Electrical_wiringForm)
def edit_Cement(request, pk):
    return edit_item(request, pk, Cement, CementForm)
def edit_Plaster(request, pk):
    return edit_item(request, pk, Plaster, PlasterForm)
def edit_Ceiling(request, pk):
    return edit_item(request, pk, Ceiling, CeilingForm)
def edit_Paint(request, pk):
    return edit_item(request, pk, Paint, PaintForm)
def edit_Fire_suppression_equip(request, pk):
    return edit_item(request, pk, Fire_suppression_equip, Fire_suppression_equipForm)
def edit_HVAC(request, pk):
    return edit_item(request, pk, HVAC, HVACForm)
def edit_Masonry(request, pk):
    return edit_item(request, pk, Masonry, MasonryForm)
def edit_Plastic(request, pk):
    return edit_item(request, pk, Plastic, PlasticForm)
def edit_Plumbing(request, pk):
    return edit_item(request, pk, Plumbing, PlumbingForm)




def delete_Floor(request, pk):

    template = 'web_app/dashboard.html'
    Floor.objects.filter(id=pk).delete()

    items = Floor.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Concrete(request, pk):

    template = 'web_app/dashboard.html'
    Concrete.objects.filter(id=pk).delete()

    items = Concrete.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
 

def delete_Insulation(request, pk):

    template = 'web_app/dashboard.html'
    Insulation.objects.filter(id=pk).delete()

    items = Insulation.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
    

def delete_Electrical_wiring(request, pk):

    template = 'web_app/dashboard.html'
    Electrical_wiring.objects.filter(id=pk).delete()

    items = Electrical_wiring.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Cement(request, pk):

    template = 'web_app/dashboard.html'
    Cement.objects.filter(id=pk).delete()

    items = Cement.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Ceiling(request, pk):

    template = 'web_app/dashboard.html'
    Ceiling.objects.filter(id=pk).delete()

    items = Ceiling.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Paint(request, pk):

    template = 'web_app/dashboard.html'
    Paint.objects.filter(id=pk).delete()

    items = Paint.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
    

def delete_Fire_suppression_equip(request, pk):

    template = 'web_app/dashboard.html'
    Fire_suppression_equip.objects.filter(id=pk).delete()

    items = Fire_suppression_equip.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Plaster(request, pk):

    template = 'web_app/dashboard.html'
    Plaster.objects.filter(id=pk).delete()

    items = Plaster.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_HVAC(request, pk):

    template = 'web_app/dashboard.html'
    HVAC.objects.filter(id=pk).delete()

    items = HVAC.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
    

def delete_Masonry(request, pk):

    template = 'web_app/dashboard.html'
    Masonry.objects.filter(id=pk).delete()

    items = Masonry.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Plastic(request, pk):

    template = 'web_app/dashboard.html'
    Plastic.objects.filter(id=pk).delete()

    items = Plastic.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Plumbing(request, pk):

    template = 'web_app/dashboard.html'
    Plumbing.objects.filter(id=pk).delete()

    items = Plumbing.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
    
