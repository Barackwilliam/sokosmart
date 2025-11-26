from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.models import ContentType
import uuid
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category_image = models.CharField(('category_image'), 
        max_length=255, 
        blank=True, 
        null=True,
        help_text=('Uploadcare UUID for category image')
    )
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    
     # ADDED: Uploadcare URL methods
    def get_image_url(self):
        """Get optimized image URL for frontend display"""
        if self.category_image:
            return f"https://ucarecdn.com/{self.category_image}/-/format/jpg/-/quality/smart/"
        return None
    
    def get_image_preview_url(self):
        """Get preview image URL for category listing"""
        if self.category_image:
            return f"https://ucarecdn.com/{self.category_image}/-/resize/300x300/-/format/jpg/-/quality/smart/"
        return None
    
    def get_og_image_url(self):
        """Get Open Graph optimized image URL"""
        if self.category_image:
            return f"https://ucarecdn.com/{self.category_image}/-/resize/1200x630/-/format/auto/"
        return None



# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.CharField(('profile_pic'), 
        max_length=255, 
        blank=True, 
        null=True,
        help_text=('Uploadcare UUID for profile image')
    )
    
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
    product_image = models.CharField(('product_image'), 
        max_length=255, 
        blank=True, 
        null=True,
        help_text=('Uploadcare UUID for product image')
    )
    
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.product_image}/-/resize/1200x630/-/format/auto/"

    def get_image_url(self):
        return f"https://ucarecdn.com/{self.product_image}/-/format/jpg/-/quality/smart/"


from ecom.models import Category, Product

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
    is_guest_order = models.BooleanField(default=False)  # Add this line
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.TextField()
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
