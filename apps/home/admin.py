
from django.contrib import admin

from .models import *

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Purchases)
admin.site.register(Marketplaces)
admin.site.register(Stores)
admin.site.register(Store_fees)
admin.site.register(Skus)
admin.site.register(Transactions)
admin.site.register(Transaction_fees)