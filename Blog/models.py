from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_countries.fields import CountryField

class Product(models.Model):
	name = models.CharField(max_length = 70)
	desc = models.TextField()
	image = models.ImageField(upload_to = 'Product_image/')
	price = models.DecimalField(max_digits = 5 , decimal_places = 1)
	country = CountryField()
	slug = models.SlugField(blank = True , null = True)
	created = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.name
	def save(*args , **kwasgs):
		if not self.slug:
			self.slug = slugify(self.slug)
		super(Product, self).save(*args , **kwasgs)


