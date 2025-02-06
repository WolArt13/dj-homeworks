from django.contrib import admin
from .models import Product, Stock, StockProduct

# Модель для отображения продуктов
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # отображение полей в списке
    search_fields = ('title', 'description')  # поиск по этим полям

# Модель для отображения складов
class StockAdmin(admin.ModelAdmin):
    list_display = ('address',)  # отображение адреса склада в списке
    search_fields = ('address',)  # поиск по адресу

# Модель для отображения связи между складом и продуктом
class StockProductAdmin(admin.ModelAdmin):
    list_display = ('stock', 'product', 'quantity', 'price')  # отображаем связь и количество
    list_filter = ('stock', 'product')  # фильтрация по складу и продукту

# Регистрация моделей
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockProduct, StockProductAdmin)
