from django.contrib import admin
from django.utils.html import format_html
from .models import Product
from unfold.admin import ModelAdmin

# Custom admin for Product
class ProductAdmin(ModelAdmin):
    list_display = ('product_name', 'image_tag')  # Show image in list

    # Method to display image
    def image_tag(self, obj):
        if obj.image:  # Check if image exists
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

# Register using custom admin
admin.site.register(Product, ProductAdmin)
