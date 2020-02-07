from django.contrib import admin

# Register your models here.

from .models import user_reg

admin.site.register(user_reg)


from .models import recipe_table

admin.site.register(recipe_table)