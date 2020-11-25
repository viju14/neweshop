from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password




# Create your views here.

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        # validation
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email
        }

        error_message = self.validation(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'msg': error_message,
                'values': value

            }
            return render(request, 'signup.html', data)

    def validation(self, customer):

        error_message = None
        if not customer.first_name:
            error_message = 'first name field is required'
        elif len(customer.first_name) < 2:
            error_message = 'lenght of the first name should be grater than 2'
        elif not customer.last_name:
            error_message = 'last name field required'
        elif not customer.phone:
            error_message = 'phone no required'
        elif len(customer.phone) < 10:
            error_message = 'phone no should be 10 digit'
        elif len(customer.email) < 4:
            error_message = 'length of email should be gater than 4'
        elif len(customer.password) < 6:
            error_message = 'length of password should be grater than 6'
        elif customer.isExists():
            error_message = 'email already present... cannot create account'
        return error_message
