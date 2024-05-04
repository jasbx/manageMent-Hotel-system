from django.shortcuts import redirect, render

from .models import *
# Create your views here.
def index(request):
    
    if request.method=='POST':
        
        name=request.POST.get('name')
        birthday=request.POST.get('birthday')
        salary=request.POST.get('salary')
        age=request.POST.get('age')
        save=Employess(name=name,birthday=birthday,salary=salary,age=age)
        if save is not None:
            save.save()
        else:
            return render(request, 'index.html')
        
        
        
        return render(request, 'index.html')
    employess=Employess.objects.all()
    myEmployess={
            'employess':employess,
            
        }
    return render(request, 'index.html',context=myEmployess)

def customers(request):

    if request.method=='POST':
        
        name=request.POST.get('name')
        id_number=request.POST.get('id_number')
        customer_number=request.POST.get('customer_number')
    
        save=Customers(name=name,customer_number=customer_number,id_number=id_number)
        if save is not None:
            save.save()
        else:
            return render(request, 'form.html')
        
        
        
        return render(request, 'form.html')
    customers=Customers.objects.all()
    mycustomers={
            'Customers':customers,
            
        }
    return render(request, 'form.html',context=mycustomers)



def reservations(request):

    if request.method=='POST':
        
        reservations_date=request.POST.get('reservations_date')
        room_number=request.POST.get('room_number')
        end_date=request.POST.get('end_date')
        squence_number=request.POST.get('squence_number')
    
        save=Reservations(reservations_date=reservations_date,room_number=room_number,end_date=end_date,squence_number=squence_number)
        if save is not None:
            save.save()
        else:
            return render(request, 'reservations.html')
        
        
        
        return render(request, 'reservations.html')
    reservations=Reservations.objects.all()
    myreservations={
            'reservations':reservations,
            
        }
    return render(request, 'reservations.html',context=myreservations)





def meals(request):

    if request.method=='POST':
        
        price=request.POST.get('price')
        meal_name=request.POST.get('meal_name')
        meal_code=request.POST.get('meal_code')
        description=request.POST.get('description')
    
        save=Meals(price=price,meal_name=meal_name,meal_code=meal_code,description=description)
        if save is not None:
            save.save()
        else:
            return render(request, 'meals.html')
        
        
        
        return render(request, 'meals.html')
    meals=Meals.objects.all()
    mymeals={
            'meals':meals,
            
        }
    return render(request, 'meals.html',context=mymeals)
