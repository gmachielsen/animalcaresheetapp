from django.contrib import admin
from .models import Animal, AnimalImages

# admin.site.register(Animal)

class AnimalImageInline(admin.TabularInline):
    model = AnimalImages
    extra = 5
class AnimalAdmin(admin.ModelAdmin):
    inlines = [ AnimalImageInline ]

admin.site.register(Animal, AnimalAdmin)
# admin.site.register(AnimalImages)
