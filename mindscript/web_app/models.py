from django.db import models

# Create your models here.

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


class Steel_framing (Material):
    pass
class Floors(Material):
    pass
class Concrete(Material):
    pass
class Lift(Material):
    pass
class Composites(Material):
    pass
class Insulation(Material):
    pass
class Coating(Material):
    pass
class Door(Material):
    pass
class Plugs_sockets(Material):
    pass
class Electrical_wiring(Material):
    pass
class Switches(Material):
    pass
class gypsum_board(Material):
    pass
class Cement(Material):
    pass
class Plaster(Material):
    pass
class Ceiling(Material):
    pass
class Flooring_tiles(Material):
    pass
class Wall_covering(Material):
    pass
class Paint(Material):
    pass
class Fire_suppression_equip(Material):
   pass
class HVAC(Material):
    pass
class Masonry(Material):
    pass
class Plastics(Material):
    pass
class Plumbing(Material):
    pass


