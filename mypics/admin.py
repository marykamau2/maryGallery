from django.contrib import admin

# Register your models here.
from .models import Category, Location, Owner, Photo

# Register your models here.
admin.site.register(Owner)
admin.site.register(Photo)
admin.site.register(Location)
admin.site.register(Category)