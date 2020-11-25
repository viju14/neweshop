from django.contrib import admin
from django.urls import path
from store.views import home, login, signup ,cart,checkout,orders
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup/', signup.Signup.as_view(), name='signup'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.logout, name='logout'),
    path('cart/', cart.Cart.as_view(), name='cart'),
    path('check-out/', checkout.CheckOut.as_view(),name='checkout'),
    path('orders/', auth_middleware(orders.OrderView.as_view()), name='orders')

]

