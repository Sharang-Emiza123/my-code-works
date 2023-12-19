from django.shortcuts import render
from django.http import HttpResponse
from .models import cities
# Create your views here.

someData = [{
    'id':1,
    'name':'Sharang',
    'place':'Pune',
    'age':20
},
{
    'id':2,
    'name':'Rugved',
    'place':'Mumbai',
    'age':79
}]

def home(request):
    usr = request.POST.get('usrnm')
    pwd = request.POST.get('pswd')

    if usr == 'sharang':
        return render(request, 'homePage.html', {'data':someData[0]})
    elif usr == 'rugved':
        return render(request, 'homePage.html', {'data':someData[1]})
    else:
        return HttpResponse('User Not Found!!')

def rdrct(request, pk):
   city_data = cities.objects.get(id=pk)
   return render(request, 'newPage.html', {'data': city_data})
        

