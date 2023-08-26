from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from .models import shop
# def index(request):
#     return HttpResponse("PARMAR SAHILKHAN[18012021034]")


def abouteme(request):
    return render(request,'abouteme.html')
def index(request):
     return render(request,'index.html')

# def shop(request):
#     shops = shop.object.all()
#     params = { 'shop':shops}
#     return render(request, 'index.html', params)
