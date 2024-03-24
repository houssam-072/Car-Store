from django.contrib import admin
from .models import Rating, Shop


class RatingShop(admin.ModelAdmin):
    list_display = ('id', 'shop_name')
    readonly_fields = ('id',)  # If id is included here, it will be read-only

# Register your models here.
admin.site.register(Rating),
admin.site.register(Shop, RatingShop)