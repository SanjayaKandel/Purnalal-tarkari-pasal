from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import vegetable,fruit
from.forms import VegetableRegistrationForm, UpdateVegetableForm, FruitRegistrationForm, UpdateFruitForm


# Create your views here.
def index(request):
    vegetables = vegetable.objects.all()
    fruits = fruit.objects.all()
    
    grocery = {
        "veg":vegetables,
        "fruits":fruits
    }
    
    return render(request, 'Home/index.html', grocery)
def retrive_veg(request, id):
    veges = vegetable.objects.get(pk=id)
    details ={
        'veg':veges,
        
    }
    return render(request, 'Home/retrive.html',details)
# #Adding vegetables
# def add_veg(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         veges = vegetable(name= name, quantity = quantity, price = price)
#         veges.save()
        
#         return HttpResponse("Tarkari darta safal vayo!!")
#     else:
#         return render(request,'Home/add_veg.html')

# def update_veg(request, id):
#     veges = vegetable.objects.get(pk=id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
        
#         veges.name=name
#         veges.quantity=quantity
#         veges.price=price
#         veges.save()
#         return HttpResponse("Tarkari safalta purbak paribartan vayo!!")
#     else:
#         return render(request, 'Home/add_veg.html', {'veges' : veges})
    
# #Adding fruits
# def add_fruit(request):
#     if request.method == 'POST':
#         fname = request.POST.get('name')
#         fquantity = request.POST.get('quantity')
#         fprice = request.POST.get('price')
#         fruits = fruit(name= fname, quantity = fquantity, price = fprice)
#         fruits.save()
        
#         return HttpResponse("Falful darta safal vayo!!")
#     else:
#         return render(request,'Home/add_fruit.html')

# #Update Fruits

# def update_fruit(request, id):
#     fruits = fruit.objects.get(pk=id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         fruits.name=name
#         fruits.quantity=quantity
#         fruits.price=price
#         fruits.save()
#         return HttpResponse("Falful safalta purbak paribartan vayo!!")
#     else:
#         return render(request, 'Home/add_fruit.html', {'fruits' : fruits})

#Delete veges
def delete_veg(request, id):
    veges = vegetable.objects.get(pk=id)
    veges.delete()
    return redirect('index')

#delete fruits
def delete_fruit(request, id):
    fruits = fruit.objects.get(pk=id)
    fruits.delete()
    return redirect('index')

def add_veg(request):
    form = VegetableRegistrationForm()
    if request.method =="POST":
        form = VegetableRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Home/add_veg.html',{'form':form})


def update_veg(request, id):
    veges = vegetable.objects.get(pk=id)
    form = UpdateVegetableForm(instance=veges)
    if request.method == 'POST':
        form = UpdateVegetableForm(request.POST, instance=veges)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'Home/update_veg.html', {'form':form})

def add_fruit(request):
    form = FruitRegistrationForm()
    if request.method=='POST':
        form = FruitRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'Home/add_fruit.html',{'form':form})

def update_fruit(request, id):
    fruits = fruit.objects.get(pk=id)
    form = FruitRegistrationForm(instance=fruits)
    if request.method =='POST':
        form = FruitRegistrationForm(request.POST,instance=fruits)
        if form.is_valid():
            form.save()
            return redirect('index')
            
    return render(request,'Home/update_fruit.html', {'form':form})
                
def retrive_fruit(request, id):
    fruits = fruit.objects.get(pk=id)
    return render(request,'Home/retrive_fruit.html',{"fruits":fruits})

    
           