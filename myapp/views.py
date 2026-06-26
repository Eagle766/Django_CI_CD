from django.shortcuts import render
from django.http import HttpResponse
from . models import Food

# Create your views here.

def index(request):
    total=0
    
    if request.method == 'POST':
        food=request.POST.getlist('food[]')
        quantity=request.POST.getlist('quantity[]')
        
        
        for i , j in zip(food, quantity):
            food= Food.objects.get(name=i.title())
            print(food.calories_per_gram*int(j))

            total =total + (food.calories_per_gram*int(j))

        print("toatal calorie",total)
       
    return render(request,'myapp/index.html',{'calories': total})
