from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carshop')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='carshop_logo/', blank=False)

    def __str__(self):
        return self.name

class Car(models.Model):
    carshop = models.ForeignKey(CarShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Марка', blank=False)
    model = models.CharField(max_length=30, verbose_name='Модель', blank=False)
    category = models.CharField(max_length=30, verbose_name='Категория', blank=False)
    owner_name = models.CharField(max_length=100, verbose_name='Имя владельца', blank=False)
    year_issue = models.CharField(max_length=10, verbose_name='Год выпуска', blank=False)
    image = models.ImageField(upload_to='car_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name