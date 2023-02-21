from django.shortcuts import render ,redirect

from .models import *
from .form import Orderform
# Create your views here.
def dashbord(request):
    Customers = Customer.objects.all()
    Product = Products.objects.all()
    Orders = Order.objects.all()
    total_customer = Customers.count()
    total_order = Orders.count()
    total_delivered=Orders.filter(status='Delivered').count()
    total_panding=Orders.filter(status='Panding').count()    

    context={'cus':Customers,'pro':Product,'order':Orders,'to':total_order,'td':total_delivered,'tp':total_panding}
    return render(request,"accounts/dashbord.html",context)

def products(request):
    products = Products.objects.all()
    context={'list':products}
    return render(request,"accounts/products.html",context)

def customer(request,id):
    customers= Customer.objects.get(id=id)
    orders = customers.order_set.all()
    order_count = orders.count()
    #this use customer  and give data
    context={'cust':customers,'orders':orders,'oc':order_count}
    return render(request,"accounts/customer.html",context)

def update_order(request,id):
    order = Order.objects.get(id=id)
    form = Orderform(instance=order)
    if request.method == 'POST':
        form = Orderform(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    #    #this use customer  and give data
    context={'form':form}
    return render(request,"accounts/orderform.html",context)



def delete_order(request,id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    #    #this use customer  and give data
    context={'order':order}
    return render(request,"accounts/delete.html",context)
