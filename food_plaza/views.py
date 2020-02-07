

# Create your views here.

from django.views.decorators.csrf import csrf_protect

#@csrf_protect
from django.http import HttpResponse 
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib.auth.models import User,auth
from .models import user_reg,recipe_table
from django.forms import modelformset_factory
from django.core.files.storage import FileSystemStorage
from .forms import recipe_form
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def registration(request):
    return render(request,'registration.html')

def login(request):

    return render(request,'login.html')


def login_verify(request):

    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
           
        try:
            a=user_reg.objects.get(name=username, password=password)
            b=recipe_table.objects.all()
            print("hello",b,type(b))
            print(username,password)
            print(a.name,a.email,a.phone,a.address) 
         #   print("sssssssssssssssssssssss",b)
                                                         
            text="2"
            return render(request,'user_desk.html',{'data':a,'recipe':b,'message':text})
        except user_reg.DoesNotExist:
            text="1"
            return render(request,'login.html',{'message':text})

                
                     
                
def addData(request):
    print("Adding the data..")
    name=request.POST["fname"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    address=request.POST["address"]
    password=request.POST["password"]
    print(name,email,phone,address,password)
    savedata=user_reg(name=name,email=email,phone=phone,address=address,password=password)
    savedata.save()
    print("Added Successfully.")
    return render(request,'login.html',{'message':"2"})    







def addrecipe(request):

    text = "0"
   #ImageFormset=modelformset_factory(recipe_table,fields=('pic'))
    if request.method=='POST':
        form=recipe_form(request.POST,request.FILES)     
        if form.is_valid():
            form.save()
           # return redirect(request,'user_desk.html') 
    else:
         form=recipe_form()
    return render(request,'addrecipe.html',{'form':form}) 

        
def view_recipe(request,item):
    print(item)
    item_choosen=recipe_table.objects.get(recipe_name=item)
        





    return render(request,'view_recipe.html',{'item':item_choosen})



def filter(request):
        basis=request.POST["filter_option"]
        print(basis)
        item_choosen=recipe_table.objects.filter(recipe_name=basis)

        print(item_choosen)
        
                
        return render(request,'user_desk.html',{'recipe':item_choosen })
        


def editrecipe(request):
    
    if request.method=='POST':
        item=request.POST['filter_option']
        item_choosen=recipe_table.objects.get(recipe_name=item)
        b=recipe_table.objects.all()
        print(item_choosen)
        print(item_choosen.recipe_name)
        return render(request,'editrecipe.html',{'recipe':b,'item':item_choosen})


    else:

        b=recipe_table.objects.all()
        return render(request,'editrecipe.html',{'recipe':b})


def editing(request):
    recipe_name=request.POST['rname']
    recipe_type=request.POST['rtype']
    ingredient=request.POST['ingredient']
    description=request.POST['desc']
    process_of_making=request.POST['pom']
    print(recipe_name)

        
        #a=Employee.objects.raw('SELECT * from homePage_employee where empname = %s',[name])
        
    a=recipe_table.objects.get(recipe_name=recipe_name)
     
        
    print(a.recipe_type)
    a.recipe_name=recipe_name
    a.recipe_type=recipe_type
    a.ingredient=ingredient
    a.description=description
    a.process_of_making=process_of_making
    a.save()
    print("updated Successfully")
    return redirect(editrecipe)



       
                               