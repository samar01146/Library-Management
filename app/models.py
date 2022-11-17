from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


CHOICES =( 
    ("admin", "Admin"), 
    ("student", "Student"), 
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER REGISTRATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class User(AbstractUser):
    username = models.CharField( max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length = 20,choices = CHOICES )

    def __str__(self):
        return str(self.username)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Book(models.Model):
    book_id = models.CharField( max_length=50,unique=True , null=True)
    book_name = models.CharField(max_length=100 , blank=True,null = True)
    book_price = models.IntegerField( blank=True,null = True)
    book_author = models.CharField(max_length = 100, blank=True,null = True)
    book_dateofpublication=models.DateField(auto_now=False, auto_now_add=False, blank=True,null = True)
    add_on_date = models.DateField(default=datetime.datetime.now, blank=True)
    book_in_language=models.CharField(max_length=40, blank=True,null = True)
    add_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.book_name)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LEND BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class LendBook(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,  on_delete=models.CASCADE)
    issued_date= models.DateTimeField(default=datetime.datetime.now, blank=True)
    fine = models.IntegerField(blank=True, null=True)
    tc = models.BooleanField()

    def __str__(self):
        return str(self.book)   

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PAYMENT DONE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class PaymentDone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_done = models.BooleanField()
    total_amount = models.IntegerField(null=True)     

    def __str__(self):
        return str(self.user)




        