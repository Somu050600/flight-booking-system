from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=False)
    uset_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(default=2000-11-11,blank=False)
    passport_number = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=100,null=True,blank = False)
    phone = models.CharField(null=True,blank=False)
    address = models.CharField(max_length=200,null=True, blank=False)

    def __str__(self):
        return self.first_name

class airline (models.Model):
    Airline_id = models.AutoField(primary_key=True)
    Airline_name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=100,null=True,blank = False)
    phone = models.CharField(null=True,blank=False)

    def __str__(self):
        return self.Airline_name

class city (models.Model):
    city_id = models.AutoField(primary_key=True)
    city_code = models.CharField(max_length=5, null=False, blank=False)
    city_name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.city_name
  
class flight (models.Model):
  filght_id = models.AutoField(primary_key=True)
  airline_name = models.ForeignKey(airline, on_delete=models.CASCADE)
  arr_city = models.ForeignKey(city, on_delete=models.CASCADE,related_name='arrivals')
  des_city = models.ForeignKey(city, on_delete=models.CASCADE, related_name='departures')
  date = models.DateField(default=2023-5-13,blank=False)
  number_of_seats = models.IntegerField(null=True,blank=False)
  price = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=False)

#   def __str__(self):
#         return self.filght_id

class booking (models.Model):
  booking_id = models.AutoField(primary_key=True)
  flight_id = models.ForeignKey(flight, on_delete=models.CASCADE)
  user_id = models.ForeignKey(user, on_delete=models.CASCADE)
  order_date = models.DateField(auto_now_add=True)
  total_cost = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=False)

  def __int__(self):
        return self.booking_id