from django.db import models

# Create your models here.
class Employess(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    birthday=models.DateField()
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    
class Customers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    id_number=models.IntegerField()
    customer_number=models.IntegerField()
    def __str__(self):
        return self.name
    
# hotel

class Reservations(models.Model):
    id=models.AutoField(primary_key=True)
    reservations_date=models.DateField()
    room_number=models.IntegerField()
    end_date=models.DateField()
    squence_number=models.IntegerField()

class Meals (models.Model):
    id=models.AutoField(primary_key=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    meal_name=models.CharField(max_length=255)
    meal_code=models.CharField(max_length=55)
    description=models.TextField()







