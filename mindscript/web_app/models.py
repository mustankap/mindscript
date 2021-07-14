from django.db import models

# Create your models here.
models_array = ['Steel_framing' ,
 'Floors',
 'Concrete',
 'Lift',
 'Composites',
 'Insulation',
 'Coating',
 'Door',
 'Plugs_sockets',
 'Electrical_wiring',
 'Switches',
 'gypsum_board',
 'Cement',
 'Plaster',
 'Ceiling',
 'Flooring_tiles',
 'Wall_covering',
 'Paint',
 'Fire_suppression_equip',
 'HVAC',
 'Masonry',
 'Plastics',
 'Plumbing',]
class Material(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Floor(Material):
    pass
class Concrete(Material):
    pass
class Insulation(Material):
    pass
class Electrical_wiring(Material):
    pass
class Cement(Material):
    pass
class Plaster(Material):
    pass
class Ceiling(Material):
    pass
class Paint(Material):
    pass
class Fire_suppression_equip(Material):
   pass
class HVAC(Material):
    pass
class Masonry(Material):
    pass
class Plastic(Material):
    pass
class Plumbing(Material):
    pass


