from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(
        max_length=100,
        default='fa-solid fa-tag',
        help_text='Font Awesome class, ví dụ: fa-solid fa-laptop'
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    