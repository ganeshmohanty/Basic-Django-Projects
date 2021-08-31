from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ( 'Assam', 'Assam'), 
    ('Arunachal Pradesh','Arunachal Pradesh' ),
    ('Bihar','Bihar'),
    ('Goa','Goa'),
    (' Gujarat', 'Gujarat'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ( 'Jharkhand','Jharkhand'),
    ( 'West Bengal','West Bengal'),
    ( 'Karnataka','Karnataka'),
    ( 'Kerala','Kerala' ),
    ('Madhya Pradesh','Madhya Pradesh'),
    ( 'Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Orissa','Orissa'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan' ),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Tripura','Tripura'),
    ('Uttaranchal','Uttaranchal'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Chhattisgarh' ,'Chhattisgarh'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)
GENDER = (
    ('Men','Men'),
    ('Women','Women')
)
MAIN_CAT = (
    ('Electronics','Electronics'),
    ('Fashion','Fashion')
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=7)
    product_image = models.ImageField(upload_to='productimg')
    rate=models.IntegerField(default=5)
    Gender = models.CharField(choices=GENDER,max_length=10,default='Men')
    main_category = models.CharField(choices=MAIN_CAT,max_length=20,default='Fashion')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    #def __str__(self):
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price

    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="users")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    star = models.IntegerField(default=1)
    date_reviewed = models.DateTimeField(auto_now_add=True)

    @property
    def star_is(self):
        rating=0
        rating_obj = Review.objects.filter(product=self.product)
        
        for i in rating_obj:
            rating += i.star
            
        rating = rating/len(rating_obj)
        
        rating = int(rating)
        return rating
