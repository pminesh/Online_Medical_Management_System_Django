"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Medical_Management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls',namespace='cart')),
    path('orders/', include('orders.urls',namespace='orders')),
    path('',views.index),
    path('master', views.master),
    path('registration', views.registration),
    path('login1', views.login1, name="login1"),
    path('header', views.header),
    path('about', views.about),
    path('contact', views.contact),
    path('contact_data', views.contact_data),
    path('services', views.services),
    path('product',views.product),
    path('product_detail/<int:id>', views.product_detail, name="product_detail"),
    path('supplier_registration', views.supplier_registration),
    path('supplierinsert', views.supplierinsert),
    path('user_registration', views.user_registration),
    path('userinsert', views.userinsert),
    path('tablets', views.tablets),
    path('inhaler', views.inhaler),
    path('injection', views.injection),
    path('capsules', views.capsules),
    path('drops', views.drops),
    path('logout1', views.logout1, name="logout1"),
    path('logout2', views.logout2, name="logout2"),

    path('index1',views.index1),
    path('about1', views.about1),
    path('contact1', views.contact1),
    path('services1', views.services1),
    path('product1',views.product1),
    path('Cust_master', views.Cust_master),

    #admin side url
    path('admin/dashboard', views.dashboard,name="dashboard"),
    path('admin/admin_master', views.admin_master,name="admin_master"),
    path('admin/signin', views.signin,name="signin"),
    path('admin/add_category', views.add_category,name="add_category"),
    path('admin/category_list',views.category_list,name="category_list"),
    path('admin/edit_category/<int:id>', views.edit_category, name="edit_category"),
    path('admin/update_category/<int:id>', views.update_category, name="edit_category"),
    path('admin/delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('admin/category_data',views.category_data,name="category_data"),
    path('admin/add_supplier', views.add_supplier,name="add_supplier"),
    path('admin/edit_supplier/<int:id>', views.edit_supplier, name="edit_supplier"),
    path('admin/update_supplier/<int:id>', views.update_supplier, name="update_supplier"),
    path('admin/delete_supplier/<int:id>', views.delete_supplier, name="delete_supplier"),
    path('admin/supplier_data',views.supplier_data,name="supplier_data"),
    path('admin/supplier_list',views.supplier_list,name="supplier_list"),
    path('admin/add_medicine', views.add_medicine,name="add_medicine"),
    path('admin/medicine_list',views.medicine_list,name="medicine_list"),
    path('admin/edit_medicine/<int:id>', views.edit_medicine, name="edit_medicine"),
    path('admin/update_medicine/<int:id>', views.update_medicine, name="update_medicine"),
    path('admin/delete_medicine/<int:id>', views.delete_medicine, name="delete_medicine"),
    path('admin/add_customer',views.add_customer,name="add_customer"),
    path('admin/edit_cust/<int:id>', views.edit_cust, name="edit_cust"),
    path('admin/update_cust/<int:id>', views.update_cust, name="update_cust"),
    path('admin/delete_cust/<int:id>', views.delete_cust, name="delete_cust"),
    path('admin/cust_data',views.cust_data,name="cust_data"),
    path('admin/customer_list',views.customer_list,name="customer_list"),
    path('admin/feedback', views.feedback,name="feedback"),
    path('admin/delete_feedback/<int:id>', views.delete_feedback, name="delete_feedback"),
    path('admin/admin_logout', views.admin_logout,name="admin_logout"),

    #supplier side url
    path('Supplier/supplier_master', views.supplier_master),
    path('Supplier/supplier_dashboard', views.supplier_dashboard),
    path('Supplier/supplier_add_customer',views.supplier_add_customer,name="supplier_add_customer"),
    path('Supplier/supplier_edit_cust/<int:id>', views.supplier_edit_cust, name="supplier_edit_cust"),
    path('Supplier/supplier_update_cust/<int:id>', views.supplier_update_cust, name="supplier_update_cust"),
    path('Supplier/supplier_delete_cust/<int:id>', views.supplier_delete_cust, name="supplier_delete_cust"),
    path('Supplier/supplier_cust_data',views.supplier_cust_data,name="supplier_cust_data"),
    path('Supplier/supplier_customer_list',views.supplier_customer_list,name="supplier_customer_list"),
    path('Supplier/supplier_add_medicine',views.supplier_add_medicine,name="supplier_add_medicine"),
    path('Supplier/supplier_medicine_list',views.supplier_medicine_list,name="supplier_medicine_list"),
    path('Supplier/supplier_medical_data', views.supplier_medical_data, name="supplier_medical_data"),
    path('Supplier/manage_order',views.manage_order,name="manage_order"),
    path('Supplier/supplier_view_order/<int:id>', views.supplier_view_order, name="supplier_view_order"),
    path('Supplier/supplier_feedback', views.supplier_feedback, name="supplier_feedback"),
    path('Supplier/supplier_delete_feedback/<int:id>', views.supplier_delete_feedback, name="supplier_delete_feedback"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
