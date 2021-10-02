from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Category(models.Model):
    	
	CatName = models.CharField(max_length=200,db_index=True,verbose_name=_("Name"))
	slug = models.SlugField(max_length=200,db_index=True,unique=True,verbose_name=_("slug"))

	

	class Meta:
		ordering = ('CatName',)
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

	def __str__(self):
		return self.CatName
	
	
	
	
	def get_absolute_url(self):
    		return reverse('shop:product_list_category',args=[self.slug])


class Product(models.Model):
    
	PrdCategory 	= models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE,verbose_name=_("Category"))
	PrdName 		= models.CharField(max_length=200,db_index=True,verbose_name=_("Name"))
	slug 			= models.SlugField(max_length=200,db_index=True,verbose_name=_("Slug"))
	PrdImage 		= models.ImageField(blank=True,upload_to='products/',verbose_name=_("Image"))
	PrdDescription  = models.TextField(blank=True,verbose_name=_("Description"))
	PrdPrice 		= models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Price"))
	PrdOldPrice 	= models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_("Old Price"))
	PrdStock 		= models.PositiveIntegerField(verbose_name=_("Stock"))
	PrdAvailable 	= models.BooleanField(default=True,verbose_name=_("Available"))
	PrdCreated 		= models.DateTimeField(auto_now_add=True,verbose_name=_("Created At"))
	PrdUpdated 		= models.DateTimeField(auto_now=True,verbose_name=_("Updated At"))

	class Meta:
		ordering = ('-PrdCreated',)
		index_together = (('id','slug'),)
		verbose_name = _("Product")
		verbose_name_plural = _("Products")

	def __str__(self):
		return self.PrdName

	

	def get_absolute_url(self):
    		return reverse('shop:product_detail',kwargs={"id":self.id,"slug": self.slug})
