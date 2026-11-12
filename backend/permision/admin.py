from django.contrib import admin
from .models import Article, Product, CustomUser

admin.site.register(Article)
admin.site.register(Product)
admin.site.register(CustomUser)
