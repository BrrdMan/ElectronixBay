from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('smartphones', 'Smartphones'),
        ('tv and home', 'TV and Home Entertainment'),
        ('audio', 'Audio'),
        ('camera', 'Camera'),
        ('computer', 'Computer Peripherals'),
        ('laptops', 'Laptops'),
        ('tablets', 'Tablets'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name