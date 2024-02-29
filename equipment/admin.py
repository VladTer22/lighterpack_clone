from django.contrib import admin
from .models import Category, Item, ItemList

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemList)
