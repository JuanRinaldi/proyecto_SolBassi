from django.db import models

class Product(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False,blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle