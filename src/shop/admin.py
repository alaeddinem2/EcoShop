from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('CatName','slug',)
	prepopulated_fields = {'slug':('CatName',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	'''
		Admin View for Product
	'''
	list_display = ('PrdName','slug','PrdCategory','PrdPrice','PrdOldPrice','PrdStock','PrdAvailable','PrdCreated','PrdUpdated',)
	list_filter = ('PrdAvailable','PrdCreated','PrdUpdated','PrdCategory',)
	list_editable = ('PrdPrice','PrdOldPrice','PrdStock','PrdAvailable',)
	prepopulated_fields = {'slug':('PrdName',)}

admin.site.register(Product, ProductAdmin)
