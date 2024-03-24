from django.db import models
from accounts.models import User



def image_upload(instance, filename):
    filename, extension = filename.split('.')
    return "%s/%s.%s"%(instance.__class__.__name__ ,str(instance.id),extension) 

CHOICES = (
    ('1', '1 star'),
    ('2', '2 star'),
    ('3', '3 star'),
    ('4', '4 star'),
    ('5', '5 star'),
)
# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to=image_upload)
    location = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.shop_name
    
class Rating(models.Model):
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE, related_name = 'rating')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.CharField(max_length = 255,choices = CHOICES)
    comment = models.CharField(max_length = 255)
    user_name = models.CharField(max_length=255)  # New field for user's name

    def __str__(self):
        return f"{self.user}'s {self.rating} star rating for {self.shop}"
    def save(self, *args, **kwargs):
        self.user_name =  f"{self.user.first_name} {self.user.last_name}"  # Assuming 'first_name' is the field in User model storing the user's name
        super(Rating, self).save(*args, **kwargs)