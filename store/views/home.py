from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


# Create your views here.

class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove= request.POST.get('remove')
        # print(product)
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)  # after adding prod in cart n then press add to cart qty should be increase
            if quantity :
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
        # print('request received')
        # return HttpResponse('<h1>index page</h1>')
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories
        # print(request.session.get('email'))
        # print(request.session.get('id'))  #nahi yet h ithe mail id

        return render(request, 'index.html', data)

        # return HttpResponse("hii")