from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Register your models here.
class AdminProdect(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

admin.site.register(Product, AdminProdect)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
