from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=6,default=0.0)

    def __str__(self):
        return self.name

