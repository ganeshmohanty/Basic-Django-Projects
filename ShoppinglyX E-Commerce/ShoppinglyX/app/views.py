from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages 
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime

class ProductView(View):
    def get(self,request):
        totalitem=0
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles})
#def home(request):
 #return render(request, 'app/home.html')

class ProductViewDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        review= Review.objects.filter(product=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:

            item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart,'reviews':review})
#def product_detail(request):
 #return render(request, 'app/productdetail.html')

@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shiping_amount=70.00
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount+=tempamount
                totalamount=shiping_amount+amount
            return render(request,'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')

@login_required
def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        totalitem = len(Cart.objects.filter(user=request.user))

        amount=0.0
        shiping_amount=70.00
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount+=tempamount
                
            data ={
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':shiping_amount+amount,
                    'totalitem':totalitem
                }
            return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shiping_amount=70.00
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount+=tempamount
                
            data ={
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':shiping_amount+amount
                }
            return JsonResponse(data)

@login_required
def remove_cart(request):
    
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        
        c.delete()
        amount=0.0
        shiping_amount=70.00
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.discounted_price)
                amount+=tempamount
                
                
        data ={
                        'amount':amount,
                        'totalamount':shiping_amount+amount
                    }
                
        return JsonResponse(data)
'''
@login_required
def buy_now(request,pk):
    
    return render(request, 'app/buynow.html')
'''

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,"active":'btn-primary'}) 

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulation Profile SucessFully Updated')
        return render(request,'app/profile.html',{'form':form,"active":'btn-primary'})
#def profile(request):
 #return render(request, 'app/profile.html')

@login_required
def address(request,pk=None):
    if pk is not None:
        Customer.objects.get(id=pk).delete()
    add = Customer.objects.filter(user=request.user)

    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'order_placed':op})

#def change_password(request):
 #return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data=='MI' or data=='Apple' or data=='Samsung' or data=="Vivo" or data=='OPPO' or data=='OnePlus' :
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=20000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=20000)
    
    return render(request, 'app/mobile.html',{'mobiles':mobiles})

#def login(request):
 #return render(request, 'app/login.html')

class CustomerRegistraionView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation!! Registration Successfull')
            form.save()  
        return render(request,'app/customerregistration.html',{'form':form})
#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

@login_required
def checkout(request,pk=None):
    if pk is not None:
        user=request.user
        if Cart.objects.filter(product=pk).exists():
            pass
        else:

            product=Product.objects.get(id=pk)
            Cart(user=user,product=product).save()
    
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shiping_amount=70.00
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:
            tempamount=(p.quantity*p.product.discounted_price)
            amount+=tempamount
        total_amount=shiping_amount+amount
    return render(request, 'app/checkout.html',{'add':add,'totalamount':total_amount,'cart_items':cart_items}) 

@login_required
def payment_done(request):
    custid = request.GET.get('custid')
    user = request.user
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')


def search(request):
    searchquery = request.GET.get('search')
    products = Product.objects.filter(Q(title__icontains=searchquery)|Q(brand__icontains=searchquery)|Q(category__icontains=searchquery)|Q(description__icontains=searchquery))
    print(products)
    print(searchquery)
    return render(request,'app/search.html',{'products':products})

def review(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            sender = request.user
            review=request.POST['review']
            pid = request.POST['pid']
            product=Product.objects.get(id=pid)
            star = request.POST['star']
            if Review.objects.filter(Q(user=sender)&Q(product=pid)).exists():
                return JsonResponse({'status':'exists'})
            rev = Review(user=sender,product=product,review=review ,star=star)
            rev.save()
            rate = int(rev.star_is)
            
            Product.objects.filter(id=pid).update(rate=rate)
            reviews = Review.objects.filter(product=pid).values('user__username','review', 'date_reviewed','star')

            
            da=list(reviews)
            
            return JsonResponse({'status':'save','reviews':da})
        return JsonResponse({'status':'no'})

def fashion(request,data=None):
    if data is not None:
        if data == 'all':
            product=Product.objects.filter(main_category='Fashion')
        elif data=='men':
            product = Product.objects.filter(Q(main_category='Fashion') & Q(Gender='Men'))
            
        elif data=='women':
            product = Product.objects.filter(Q(main_category='Fashion') & Q(Gender='Women'))
            
    else:
        product = Product.objects.filter(main_category='Fashion')
    return render(request,'app/fashion.html',{'fashion':product})
'''
def fashionfilter(request,rate):
    pk = rate
    if pk==4:
        product=Product.objects.filter(rate__gte=pk)
    elif pk==3:
        product=Product.objects.filter(rate__gte=pk)
    elif pk==2:
        product=Product.objects.filter(rate__gte=pk)
    elif pk==1:
        product=Product.objects.filter(rate__gte=pk)
    return render(request,'app/fashion.html',{'fashion':product})
'''