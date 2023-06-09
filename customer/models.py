from django.db import models
from django.contrib.auth import login
from Book.models import Books
from django.contrib.auth.models import User
from datetime import timedelta,datetime


# Create your models here.
class Carts(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    options = (
        ("incart", "incart"),
        ("orderplaced", "orderplaced"),
        ("ordercancelled", "ordercancelled")
    )
    status = models.CharField(max_length=20, choices=options, default="incart")


class Orders(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True,null=True)
    edate = datetime.today()+timedelta(days=5)
    expected_delivery_date = models.DateField(default=edate,null=True)
    options=(
        ("order_placed","order_placed"),
        ("dispatch","dispatch"),
        ("in_transit","in_transit"),
        ("delivered","delivered"),
        ("order_cancelled","order_cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="order_placed")

class Review(models.Model):
    comment=models.CharField(max_length=120)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Books,on_delete=models.CASCADE,related_name="reviews")
    options=(
        ("2","2"),("2.5","2.5"),("3","3"),("3.5","3.5"),("4","4"),
        ("4.5","4.5"),("5","5")
    )
    rating=models.CharField(max_length=120,choices=options)



