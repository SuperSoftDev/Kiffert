from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=100, blank=True, default="",db_column="Email")
    password = models.CharField(max_length=255, blank=True, default="",db_column="Password")
    tier = models.CharField(max_length=45, blank=True, default="",db_column="Account Tier")
    def __str__(self):
        return self.email

class Products(models.Model):
    user_id = models.ForeignKey(Users, related_name='users_products', on_delete=models.CASCADE,db_column="UserID")
    name = models.CharField(max_length=100,blank=True,default="",db_column="Product Name")
    def __str__(self):
        return self.name

class Purchases(models.Model):
    date = models.DateField(auto_now_add=True,db_column="Date")
    product_id = models.ForeignKey(Products, related_name='products_purchases', on_delete=models.CASCADE,db_column="ProductID")
    quantity = models.PositiveIntegerField(default = 0,db_column="Quantity")    
    unit_cost = models.DecimalField(default = 0,max_digits=10, decimal_places=2,db_column="Unit Cost")
    def __str__(self):
        return str(self.product_id)

class Marketplaces(models.Model):
    name = models.CharField(max_length=100, blank=True, default="",db_column="Name")
    connection_method = models.CharField(max_length=45, blank=True, default="",db_column="Connection Method")    
    def __str__(self):
        return str(self.name)

class Stores(models.Model):
    marketplace_id = models.ForeignKey(Marketplaces, related_name='marketplaces_stores', on_delete=models.CASCADE,db_column="MarketplaceID")
    user_id = models.ForeignKey(Users, related_name='users_stores', on_delete=models.CASCADE,db_column="UserID")
    name = models.CharField(max_length=100, blank=True, default="",db_column="Name")
    api_key = models.CharField(max_length=255, blank=True, default="",db_column="Api Key")
    user_key = models.CharField(max_length=255, blank=True, default="",db_column="User Key")
    store_key = models.CharField(max_length=255, blank=True, default="",db_column="Store Key")
    def __str__(self):
        return str(self.name)

class Store_fees(models.Model):
    store_id = models.ForeignKey(Stores, related_name='stores_store_fees', on_delete=models.CASCADE,db_column="StoreID")
    date = models.DateField(auto_now_add=True,db_column="Date")
    type = models.CharField(max_length=100, blank=True, default="",db_column="Type")
    description = models.CharField(max_length=100, blank=True, default="",db_column="Description")
    amount = models.DecimalField(default = 0,max_digits=10, decimal_places=2,db_column="Amount")
    def __str__(self):
        return str(self.date)

class Skus(models.Model):
    store_id = models.ForeignKey(Stores, related_name='stores_skus', on_delete=models.CASCADE,db_column="StoreID")
    sku = models.CharField(max_length=255,blank=True,default="",db_column="Sku")
    product_id = models.ForeignKey(Products, related_name='products_skus', on_delete=models.CASCADE,db_column="ProductID")
    def __str__(self):
        return self.sku

class Transactions(models.Model):
    type = models.CharField(max_length=100, blank=True, default="",db_column="Type")
    date = models.DateField(auto_now_add=True,db_column="Date")
    sku_store_id = models.ForeignKey(Skus, related_name='skus_transactions', on_delete=models.CASCADE,db_column="Sku-StoreID")
    sku_sku = models.CharField(max_length=255,blank=True,default="",db_column="Sku_Sku")
    quantity = models.PositiveIntegerField(default = 0,db_column="Quantity")
    price = models.DecimalField(default = 0,max_digits=10, decimal_places=2,db_column="Price")
    def __str__(self):
        return self.date

class Transaction_fees(models.Model):
    transaction_id = models.ForeignKey(Transactions, related_name='transactions_transaction_fees', on_delete=models.CASCADE,db_column="TransactionID")
    date = models.DateField(auto_now_add=True,db_column="Date")
    type = models.CharField(max_length=100, blank=True, default="",db_column="Type")
    description = models.CharField(max_length=100, blank=True, default="",db_column="Description")
    amount = models.DecimalField(default = 0,max_digits=10, decimal_places=2,db_column="Amount")
    def __str__(self):
        return str(self.date)