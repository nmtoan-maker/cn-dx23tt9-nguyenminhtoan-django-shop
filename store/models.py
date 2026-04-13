from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('laptop', 'Laptop'),
        ('pc', 'PC'),
        ('monitor', 'Màn hình'),
        ('accessory', 'Phụ kiện'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='laptop')

    def __str__(self):
        return self.name