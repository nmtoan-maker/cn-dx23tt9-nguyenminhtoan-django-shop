from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'icon')
    search_fields = ('name',)

    def icon_preview(self, obj):
        return format_html(
            '<i class="{}"></i>&nbsp;'
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">',
            obj.icon
        )
    icon_preview.short_description = 'Preview'


admin.site.register(Product)
