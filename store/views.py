from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Products
#from tags.models import TagItem

# Create your views here.
def greetings(request):
  #TagItem.objects.get_tags_for(Products, 1)
  #try:
  query_set = Products.objects.filter(Q(inventory__lt=2) | Q(unit_price__lt=3))
  #except ObjectDoesNotExist:
    #pass

  # query_set = Products.objects.all()
  # for product in query_set:
  #   print(product)

  #return HttpResponse("Hi! how far na")
  #return render(request, 'hello.html', {'name': 'Mubarak'})
  return render(request, 'greet.html', {'name': 'Mubarak', 'products': list(query_set)})


