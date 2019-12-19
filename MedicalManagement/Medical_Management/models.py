from django.db import models

class Admin(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=50)
    class Meta:
        db_table='Admin'
    def __str__(self):
        return self.Username
class Category(models.Model):
    category_title=models.CharField(max_length=20)
    class Meta:
        db_table='Category'
    def __str__(self):
        return self.category_title

class Product(models.Model):
    prod_name=models.CharField(max_length=20)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    prod_photo=models.ImageField(upload_to='images/product/')
    prod_price=models.IntegerField()
    prod_description=models.TextField()
    class Meta:
        db_table='Product'
    def __str__(self):
        return self.prod_name
class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    bod = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/User/')
    class Meta:
        db_table='Customer'
    def __str__(self):
        return self.firstname

class Supplier(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    shopname = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/Supplier/')
    class Meta:
        db_table='Supplier'
    def __str__(self):
        return self.firstname

class ContactUs(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.BigIntegerField()
    message=models.TextField()
    class Meta:
        db_table='ContactUs'
    def __str__(self):
        return self.name

