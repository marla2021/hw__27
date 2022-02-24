from django.contrib import admin

# Register your models here.
from ads.models import Location, User, Category, Ad


admin.site.register(Location)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ad)