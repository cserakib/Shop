from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('home')

    def get(self, request):
        products = None
        categories = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        date = {}

        date['products'] = products
        date['categories'] = categories
        print('You are ', request.session.get('email'))
        return render(request, 'index.html', date)





def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        #validation
        value = {
            'first_name':first_name,
            'last_name' :last_name,
            'phone': phone,
            'email': email
        }

        error_message = None;

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        if (not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not last_name:
            error_message = 'Last Name Required'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not phone:
            error_message = 'Phone Number required'
        elif len(phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'

        #saving

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')
        else:

            data = {
                'error':error_message,
                'values':value,
            }

            return render(request, 'singup.html',data)

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = 'Email or Password invalid !! '
        else:
            error_message = 'Email or Password invalid !! '

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


