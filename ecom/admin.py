from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Customer, Product, Orders, Feedback, Category
from .forms import CustomerForm, ProductForm
from .forms import CategoryForm


# ========== Category Admin ==========
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'category_image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.category_image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'
    list_display = ('name', 'description')
    search_fields = ('name',)

# ========== Customer Admin ==========
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'profile_pic':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.profile_pic:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'

    list_display = ('get_name', 'mobile', 'address', 'image_preview')


# ========== Product Admin ==========
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'product_image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': '76122001cca4add87f02',
            })
        return formfield

    def image_preview(self, obj):
        if obj.product_image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'

    list_display = ('name', 'category', 'price', 'description', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name',)


# ========== Orders Admin ==========
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'email', 'mobile', 'status', 'order_date')
    list_filter = ('status', 'order_date')


# ========== Feedback Admin ==========
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback', 'date')


# ========== Register All ==========
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Feedback, FeedbackAdmin)
