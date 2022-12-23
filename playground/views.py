# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from store.models import Products

# # Create your views here.
# def say_hello(request):
#   try:
#     product = Products.objects.get(pk =0)
#   except ObjectDoesNotExist:
#     pass

#   # query_set = Products.objects.all()
#   # for product in query_set:
#   #   print(product)

#   #return HttpResponse("Hi! how far na")
#   return render(request, 'hello.html', {'name': 'Mubarak'})
