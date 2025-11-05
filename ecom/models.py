from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.models import ContentType

from cloudinary.models import CloudinaryField



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.category_image}/-/resize/1200x630/-/format/auto/"

    def get_image_url(self):
        return f"https://ucarecdn.com/{self.category_image}/-/format/jpg/-/quality/smart/"



# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic =models.CharField(max_length=255, blank=True, null=True) 
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


    
     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.profile_pic}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.profile_pic}/-/format/jpg/-/quality/smart/"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=40)
    product_image = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.product_image}/-/resize/1200x630/-/format/auto/"

    def get_image_url(self):
        return f"https://ucarecdn.com/{self.product_image}/-/format/jpg/-/quality/smart/"


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.TextField()
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
