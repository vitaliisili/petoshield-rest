from django.contrib import admin
from apps.pet import models


class CustomBreed(admin.ModelAdmin):
    list_display = (
        'name',
        'species',
        'age_min',
        'age_max',
        'risk_level',
        'get_description'
    )

    @admin.display(description="description")
    def get_description(self, obj):
        if len(obj.description) > 50:
            return f"{obj.description[:50]}..."

        return f"{obj.description[:50]}"


class CustomPet(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'gender',
        'species',
        'get_breed',
        'user'
    )

    @admin.display(description='breed')
    def get_breed(self, obj):
        return obj.breed.name


admin.site.register(models.Breed, CustomBreed)
admin.site.register(models.Pet, CustomPet)
