from django.contrib import admin
from .models import Admin,Category,Product,Customer,Supplier,ContactUs


admin.site.site_header='Admin-Medical Management System'
admin.site.site_title='Home'
admin.site.index_title='Dashboard'


class ListAdmin(admin.ModelAdmin):
    list_display = ('id','Username','Password')
    ordering = ['Username',]
    search_fields = ['Username']

@admin.register(Category)
class ListCategory(admin.ModelAdmin):
    list_display = ('id','category_title')
    ordering = ['category_title', ]
    search_fields = ['category_title']

@admin.register(Product)
class ListProduct(admin.ModelAdmin):
    list_display = ('id','prod_name','category_id','prod_photo','prod_price','prod_description')
    ordering = ('prod_name','prod_price')
    search_fields = ('prod_name','prod_price')

@admin.register(ContactUs)
class ListProduct(admin.ModelAdmin):
    list_display = ('id','name','email','mobile','message')
    ordering = ['name']
    search_fields = ('name','mobile')

@admin.register(Customer)
class ListProduct(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','gender','bod','mobile','email')
    ordering = ('firstname','lastname')
    search_fields = ('firstname','lastname')

@admin.register(Supplier)
class ListProduct(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','address','mobile','email')
    ordering = ('firstname','lastname')
    search_fields = ('firstname','lastname')



