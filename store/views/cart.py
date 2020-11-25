from django.shortcuts import render,redirect
from django.views import View
from store.models.customer import Customer
from store.models.category import Category
from store.models.product import Product
from django.contrib.auth.hashers import make_password,check_password



class Cart(View):

    def get(self , request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})

