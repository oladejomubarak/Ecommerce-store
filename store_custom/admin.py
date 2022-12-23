from django.contrib import admin
from store.admin import ProductAdmin
from tags.models import TagItem
from django.contrib.contenttypes.admin import GenericTabularInline
from store.models import Products

# Register your models here.
class TagInline(GenericTabularInline):
  autocomplete_fields = ['tag']
  model = TagItem
  #pass

class CustomProductAdmin(ProductAdmin):
  inlines =[TagInline]

admin.site.unregister(Products)
admin.site.register(Products, CustomProductAdmin)