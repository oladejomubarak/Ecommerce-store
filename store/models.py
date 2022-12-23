from django.db import models
from django.core.validators import MinValueValidator
#from tags.models import TagItem
from django.contrib.contenttypes.models import ContentType

# Create your models here.
# class TaggedItemManager(models.Manager):
#    def get_tags_for(self, obj_type, obj_id):
#     content_type= ContentType.objects.get_for_model(obj_type)
#     return TagItem.objects.select_related('tags').filter(content_type = content_type, object_id = obj_id)



class Collection(models.Model):
  title = models.CharField(max_length=255)
  featured_product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, related_name='+')

  def __str__(self) -> str:
    return self.title

  class Meta:
    ordering = ['title']

class Promotion(models.Model):
  desription = models.CharField(max_length=255)
  discount = models.FloatField()

class Products(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(null=True, blank=True)
  unit_price = models.DecimalField(
    max_digits=6, 
    decimal_places=2,
    validators=[MinValueValidator(1)])
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  promotions = models.ManyToManyField(Promotion, blank=True)

  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering = ['title']



class Customer(models.Model):
  MEMBERSHIP_GOLD = "G"
  MEMBERSHIP_SILVER = "S"
  MEMBERSHIP_BRONZE = "B"

  MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_GOLD, 'gold'),
    (MEMBERSHIP_SILVER, 'silver'),
    (MEMBERSHIP_BRONZE, 'bronze'),
  ]

  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  membership = models.CharField(max_length=1, choices= MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name}'

  class Meta:
    ordering = ['first_name', 'last_name']

class Order(models.Model):
  PAYMENT_STATUS_PENDING = "P"
  PAYMENT_STATUS_COMPLETE = "C"
  PAYMENT_STATUS_FAILED = "F"

  PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'pending'),
    (PAYMENT_STATUS_COMPLETE, 'complete'),
    (PAYMENT_STATUS_FAILED, 'failed'),
  ]

  placed_at = models.DateTimeField(auto_now_add=True)
  payment_status = models.CharField(max_length=1, choices = PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class Address(models.Model):
  City = models.CharField(max_length=255)
  street = models.CharField(max_length=255)
  customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.PROTECT)
  product = models.ForeignKey(Products, on_delete=models.PROTECT) 
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField()





