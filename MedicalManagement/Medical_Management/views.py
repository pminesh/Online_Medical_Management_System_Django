from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from cart.forms import CartAddProductForm
from .models import Category,Product,Customer,Supplier,ContactUs
from orders.models import Order,OrderItem

# ----------------------------User Side--------------------------------

def index(request):
    return render(request,"User/index.html")

def master(request):
    return render(request,"User/master.html")

def registration(request):
    return render(request,"User/registration.html")

def login1(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        return render(request, "Supplier/supplier_dashboard.html", {'supplier_email': email})
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/index1.html", {'user_email': email})
    context = {}
    if request.method == 'POST':
        U = request.POST['checkuser']
        if U == "Supplier":
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Supplier.objects.get(email=email,password= password)
            except:
                context['Error'] = "Invalid username and password"
                return render(request, "User/login.html", context)
            if user is not None:
                request.session['supplier_email'] = user.email
                return HttpResponseRedirect('Supplier/supplier_dashboard')
            else:
                context['Error'] = "Invalid username and password"
                return render(request, "User/login.html", context)
        elif U == "Customer":
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Customer.objects.get(email = email,password=password)
            except:
                context['Error'] = "Invalid username and password"
                return render(request, "User/login.html", context)
            if user is not None:
                request.session['user_email'] = user.email
                return HttpResponseRedirect('index1')
            else:
                context['Error'] = "Invalid username and password"
                return render(request, "User/login.html", context)
    else:
        return render(request, "User/login.html")

def logout1(request):
    try:
        del request.session['supplier_email']
    except:
        pass
    messages.success(request, 'You have successfully logged out..!')
    return redirect("/login1")

def logout2(request):
    try:
        del request.session['user_email']
    except:
        pass
    messages.success(request, 'You have successfully logged out..!')
    return redirect("/login1")

def header(request):
    return render(request,"User/header.html")

def about(request):
    return render(request,"User/Aboutus.html")

def contact(request):
    return render(request,"User/Contactus.html")

def contact_data(request):
    context = {}
    if request.method == "POST":
        form = ContactUs(name=request.POST['name'],email=request.POST['email'],mobile=request.POST['mobile'],message=request.POST['message'])
        try:
            form.save()
            messages.success(request, 'Successfully Inserted Record..!')
            if request.session.has_key('user_email'):
                return redirect("contact")
            else:
                return redirect("contact")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "User/Contactus.html",context)
    else:
        return render(request, "User/Contactus.html")

def services(request):
    return render(request,"User/services.html")

def product(request):
    datas=Product.objects.all()
    return render(request,"User/product.html",{'datas':datas})

def product_detail(request,id):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        product = Product.objects.get(id=id)
        cart_product_form = CartAddProductForm()
        return render(request, "User/details1.html",
                      {"user_email": email, 'product': product, 'cart_product_form': cart_product_form})
    else:
        product = Product.objects.get(id=id)
        cart_product_form = CartAddProductForm()
        return render(request,"User/details.html",{'product':product,'cart_product_form':cart_product_form})


def user_registration(request):
    return render(request,"User/user_registration.html")

def userinsert(request):
    context = {}
    if request.method=="POST":
        form = Customer(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        gender=request.POST['gender'], bod=request.POST['bod'], address=request.POST['address'],
                        city=request.POST['city'], email=request.POST['email'], password=request.POST['password'],
                        mobile=request.POST['mobile'], photo=request.FILES['img'])
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("user_registration")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "User/user_registration.html", context)


def supplier_registration(request):
    return render(request,"User/supplier_registration.html")

def supplierinsert(request):
    context = {}
    if request.method=="POST":
        form = Supplier(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        shopname=request.POST['shopname'], address=request.POST['address'],
                        city=request.POST['city'], email=request.POST['email'], password=request.POST['password'],
                        mobile=request.POST['mobile'], photo=request.FILES['img'])
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("supplier_registration")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "User/supplier_registration.html", context)

def tablets(request):
    return render(request,"User/tablets.html")

def inhaler(request):
    return render(request,"User/inhaler.html")

def injection(request):
    return render(request,"User/injection.html")

def capsules(request):
    return render(request,"User/capsules.html")

def drops(request):
    return render(request,"User/drops.html")

@login_required(login_url="login1")
def Cust_master(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/Cust_master.html",{"user_email":email})
    else:
        return render(request, "User/login.html")

def index1(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/index1.html",{"user_email":email})
    else:
        return render(request, "User/login.html")

def product1(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        datas = Product.objects.all()
        return render(request, "User/product1.html",{"user_email":email,'datas': datas})
    else:
        return render(request, "User/login.html")

def contact1(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/contact1.html",{"user_email":email})
    else:
        return render(request, "User/login.html")

def about1(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/about1.html",{"user_email":email})
    else:
        return render(request, "User/login.html")

def services1(request):
    if request.session.has_key('user_email'):
        email = request.session['user_email']
        return render(request, "User/services1.html",{"user_email":email})
    else:
        return render(request, "User/login.html")
# ----------------------------Admin Side--------------------------------

def signin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['admin_id'] = user.id
            return HttpResponseRedirect('dashboard')
        else:
            context['Error'] = "Invalid username and password"
            return render(request, "Admin/admin_login.html", context)
    else:
        return render(request, "Admin/admin_login.html")

@login_required(login_url="signin")
def admin_master(request):
    return render(request,"Admin/admin_master.html")

@login_required(login_url="signin")
def dashboard(request):
    return render(request,"Admin/dashboard.html")

@login_required(login_url="signin")
def add_category(request):
    return render(request,"Admin/add_category.html")

@login_required(login_url="signin")
def category_data(request):
    context = {}
    if request.method == "POST":
        form = Category(category_title=request.POST['title'])
        try:
            form.save()
            messages.success(request, 'Successfully Inserted Record..!')
            return redirect("add_category")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "Admin/add_category.html",context)
    else:
        return render(request,"Admin/add_category.html")

@login_required(login_url="signin")
def category_list(request):
    datas = Category.objects.all()
    return render(request,"Admin/category_list.html",{'datas':datas})

@login_required(login_url="signin")
def edit_category(request,id):
    edit = Category.objects.get(id=id)
    return render(request,"Admin/edit_category.html",{'edit': edit})

@login_required(login_url="signin")
def update_category(request,id):
    context={}
    update = Category.objects.get(id=id)
    update.category_title = request.POST.get('title')
    try:
        update.save()
        messages.success(request, 'Successfully Updated Record..!')
        return redirect("category_list")
    except:
        context['Error'] = "Not Update Record Please Try Again..!"
        return render(request, "Admin/category_list.html", context)

@login_required(login_url="signin")
def delete_category(request,id):
    context={}
    delete = Category.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("category_list")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Admin/category_list.html", context)


@login_required(login_url="signin")
def add_supplier(request):
    return render(request,"Admin/add_supplier.html")

@login_required(login_url="signin")
def supplier_data(request):
    context = {}
    if request.method=="POST":
        form = Supplier(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        shopname=request.POST['shopname'], address=request.POST['address'],
                        city=request.POST['city'], email=request.POST['email'], password=request.POST['password'],
                        mobile=request.POST['mobile'], photo=request.FILES['img'])
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("add_supplier")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "Admin/add_supplier.html", context)

@login_required(login_url="signin")
def supplier_list(request):
    datas = Supplier.objects.all()
    return render(request,"Admin/supplier_list.html",{'datas':datas})

@login_required(login_url="signin")
def edit_supplier(request,id):
    edit = Supplier.objects.get(id=id)
    return render(request,"Admin/edit_supplier.html",{'edit': edit})

@login_required(login_url="signin")
def update_supplier(request,id):
    context={}
    update = Supplier.objects.get(id=id)
    update.firstname = request.POST['firstname']
    update.lastname = request.POST['lastname']
    update.shopname = request.POST['shopname']
    update.address = request.POST['address']
    update.city = request.POST['city']
    update.email = request.POST['email']
    update.mobile = request.POST['mobile']
    update.photo = request.FILES['img']
    try:
        update.save()
        messages.success(request, 'Successfully Updated Record..!')
        return redirect("supplier_list")
    except:
        context['Error'] = "Not Update Record Please Try Again..!"
        return render(request, "Admin/supplier_list.html", context)

@login_required(login_url="signin")
def delete_supplier(request,id):
    context={}
    delete = Supplier.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("supplier_list")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Admin/supplier_list.html", context)

@login_required(login_url="signin")
def add_customer(request):
    return render(request,"Admin/add_customer.html")

@login_required(login_url="signin")
def cust_data(request):
    context = {}
    if request.method=="POST":
        form = Customer(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        gender=request.POST['gender'], bod=request.POST['bod'], address=request.POST['address'],
                        city=request.POST['city'], email=request.POST['email'], password=request.POST['password'],
                        mobile=request.POST['mobile'], photo=request.FILES['img'])
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("add_customer")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "Admin/add_customer.html", context)

@login_required(login_url="signin")
def customer_list(request):
    datas = Customer.objects.all()
    return render(request,"Admin/customer_list.html",{'datas':datas})

@login_required(login_url="signin")
def edit_cust(request,id):
    edit = Customer.objects.get(id=id)
    return render(request,"Admin/edit_cust.html",{'edit': edit})

@login_required(login_url="signin")
def update_cust(request,id):
    context={}
    update = Customer.objects.get(id=id)
    update.firstname = request.POST['firstname']
    update.lastname = request.POST['lastname']
    update.gender = request.POST['gender']
    update.bod = request.POST['bod']
    update.address = request.POST['address']
    update.city = request.POST['city']
    update.email = request.POST['email']
    update.mobile = request.POST['mobile']
    update.photo = request.FILES['img']

    try:
        update.save()
        messages.success(request, 'Successfully Updated Record..!')
        return redirect("customer_list")
    except:
        context['Error'] = "Not Update Record Please Try Again..!"
        return render(request, "Admin/customer_list.html", context)

@login_required(login_url="signin")
def delete_cust(request,id):
    context={}
    delete = Customer.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("customer_list")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Admin/customer_list.html", context)

@login_required(login_url="signin")
def add_medicine(request):
    return render(request,"Admin/add_medicine.html")

@login_required(login_url="signin")
def medicine_list(request):
    datas = Product.objects.all()
    return render(request,"Admin/medicine_list.html", {'datas': datas})

@login_required(login_url="signin")
def edit_medicine(request,id):
    edit = Product.objects.get(id=id)
    data = Category.objects.all()
    return render(request,"Admin/edit_medicine.html",{'edit': edit,'datas':data})

@login_required(login_url="signin")
def update_medicine(request,id):
    context={}
    cat_id = request.POST['category']
    update = Product.objects.get(id=id)
    update.prod_name=request.POST['prod_name']
    update.prod_photo=request.FILES['photo']
    update.prod_price=request.POST['price']
    update.prod_description=request.POST['description']
    update.category_id=Category(id=cat_id)
    try:
        update.save()
        messages.success(request, 'Successfully Updated Record..!')
        return redirect("medicine_list")
    except:
        context['Error'] = "Not Update Record Please Try Again..!"
        return render(request, "Admin/medicine_list.html", context)

@login_required(login_url="signin")
def delete_medicine(request,id):
    context={}
    delete = Product.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("medicine_list")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Admin/medicine_list.html", context)


@login_required(login_url="signin")
def feedback(request):
    datas = ContactUs.objects.all()
    return render(request,"Admin/feedback.html", {'datas': datas})

@login_required(login_url="signin")
def delete_feedback(request,id):
    context={}
    delete = ContactUs.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("feedback")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Admin/feedback.html", context)

@login_required(login_url="signin")
def admin_logout(request):
    auth.logout(request)
    try:
        del request.session['admin_id']
    except:
        pass
    messages.success(request, 'You have successfully logged out..!')
    return redirect("signin")



#------------------------------Supplier Side-----------------------------------

def supplier_master(request):
    return render(request,"Supplier/supplier_master.html")

def supplier_dashboard(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']

        return render(request, "Supplier/supplier_dashboard.html",{"supplier_email": email})
    else:
        return render(request, "User/login.html")

def supplier_cust_data(request):
    context = {}
    if request.method=="POST":
        form = Customer(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        gender=request.POST['gender'], bod=request.POST['bod'], address=request.POST['address'],
                        city=request.POST['city'], email=request.POST['email'], password=request.POST['password'],
                        mobile=request.POST['mobile'], photo=request.FILES['img'])
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("supplier_add_customer")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "Supplier/add_customer.html", context)

def supplier_add_customer(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']

        return render(request, "Supplier/add_customer.html",{"supplier_email": email})
    else:
        return render(request, "User/login.html")

def supplier_customer_list(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        datas = Customer.objects.all()
        return render(request, "Supplier/customer_list.html",{"supplier_email": email,'datas':datas})
    else:
        return render(request, "User/login.html")

def supplier_edit_cust(request,id):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        edit = Customer.objects.get(id=id)
        return render(request, "Supplier/supplier_edit_cust.html",{"supplier_email": email,'edit':edit})
    else:
        return render(request, "User/login.html")


def supplier_update_cust(request,id):
    context={}
    update = Customer.objects.get(id=id)
    update.firstname = request.POST['firstname']
    update.lastname = request.POST['lastname']
    update.gender = request.POST['gender']
    update.bod = request.POST['bod']
    update.address = request.POST['address']
    update.city = request.POST['city']
    update.email = request.POST['email']
    update.mobile = request.POST['mobile']
    update.photo = request.FILES['img']

    try:
        update.save()
        messages.success(request, 'Successfully Updated Record..!')
        return redirect("supplier_customer_list")
    except:
        context['Error'] = "Not Update Record Please Try Again..!"
        return render(request, "Supplier/customer_list.html", context)

def supplier_delete_cust(request,id):
    context={}
    delete = Customer.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("supplier_customer_list")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Supplier/customer_list.html", context)

def supplier_add_medicine(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        datas = Category.objects.all()
        return render(request, "Supplier/add_medicine.html",{"supplier_email": email,'datas':datas})
    else:
        return render(request, "User/login.html")

def supplier_medicine_list(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        datas = Product.objects.all()
        return render(request, "Supplier/medicine_list.html",{"supplier_email": email,'datas':datas})
    else:
        return render(request, "User/login.html")

def supplier_medical_data(request):
    context = {}
    if request.method=="POST":
        cat_id = request.POST['category']
        form = Product(prod_name=request.POST['prod_name'],prod_photo=request.FILES['photo'],prod_price=request.POST['price'],
                       prod_description=request.POST['description'],category_id=Category(id=cat_id),)
        print(form)
        try:
            form.save()
            messages.success(request, 'Successfully Insert Record..!')
            return redirect("supplier_add_medicine")
        except:
            context['Error'] = "Not Insert Record Please Try Again..!"
            return render(request, "Supplier/add_medicine.html", context)

def manage_order(request):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        datas =Order.objects.all()
        return render(request, "Supplier/order.html",{"supplier_email":email,"datas": datas})
    else:
        return render(request, "User/login.html")

def supplier_view_order(request,id):
    if request.session.has_key('supplier_email'):
        email = request.session['supplier_email']
        photo = Supplier.objects.get(email=email)
        view_item = OrderItem.objects.get(id=id)
        view_order = Order.objects.get(id=id)
        view_prod = Product.objects.get(id=id)
        # cust = Customer.objects.get(firstname=view.id)
        return render(request, "Supplier/supplier_view_order.html",
                      {"supplier_email": email, "photo": photo, "view_item": view_item,
                       'view_order': view_order, 'view_prod': view_prod})
    else:
        return render(request, "User/login.html")

def supplier_feedback(request):
    datas = ContactUs.objects.all()
    return render(request,"Supplier/feedback.html", {'datas': datas})

def supplier_delete_feedback(request,id):
    context={}
    delete = ContactUs.objects.get(id=id)
    try:
        delete.delete()
        messages.success(request, 'Successfully Deleted Record..!')
        return redirect("supplier_feedback")
    except:
        context['Error'] = "Not Delete Record Please Try Again..!"
        return render(request, "Supplier/feedback.html", context)