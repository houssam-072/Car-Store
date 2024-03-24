from django.db import models
from accounts.models import User
import datetime
from django.core.exceptions import ValidationError


# Create your models here.
def image_upload(instance, filename):
    filename, extension = filename.split('.')
    return "%s/%s.%s"%(instance.__class__.__name__ ,str(instance.id),extension) 

CHOICES = (
    ('Gear', 'Gear'),
    ('Automatic', 'Automatic')
)
FUEL_CHOICES = (
    ('gasoline', 'gasoline'),
    ('deizel', 'deizel')
)
BODY_CHOICES =(
    ('New','New'),
    ('Perfect','Perfect'),
    ('Good','Good'),
    ('Medium','Medium'),
    ('Bad','Bad'),
    ('So Bad',' So Bad'),
)
MECHANICS_CHOICES =(
    ('New','New'),
    ('Perfect','Perfect'),
    ('Good','Good'),
    ('Medium','Medium'),
    ('Bad','Bad'),
    ('So Bad',' So Bad'),
)
class Car(models.Model):
    # car
    car_name = models.CharField(max_length = 255, null = False)
    # brand
    brand = models.CharField(max_length = 255, null = False)
    # model
    model = models.CharField(max_length = 255, null = False)
    
    desc = models.CharField(max_length = 366)
    city = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    capacity = models.IntegerField()
    doors = models.IntegerField()
    # body Condition
    aircondition = models.CharField(max_length = 255, choices = BODY_CHOICES)
    transmition = models.CharField(max_length = 255, choices = CHOICES)
    # mechanics
    mechanics = models.CharField(max_length = 255, choices = MECHANICS_CHOICES)
    # fuel
    fuel = models.CharField(max_length = 255, choices = FUEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # year
    year = models.IntegerField(default=datetime.datetime.now().year)
    image = models.ImageField(upload_to = image_upload)
    # color
    color = models.CharField(max_length = 255, null = False)
    # millage
    millage = models.IntegerField()

    def __str__(self):
        return self.car_name
    
class BuyCar(models.Model):
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    client = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'client_buy')
    car_owner =   models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'owner_buy')
    apoinment = models.DateTimeField(auto_now = False)
    client_full_name = models.CharField(max_length = 255)
    client_mobile_phone = models.IntegerField(default = '+966')
    def __str__(self):
        return f"{self.car.car_name}-{self.client_full_name}"
    
