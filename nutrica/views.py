from email.mime import message
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
import requests
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from account.models import patientdb
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

def home(request):
    return render(request, 'nutrica/home.html')

def aboutus(request):
    return render(request, 'nutrica/aboutus.html')

def contact(request):
    return render(request, 'nutrica/contact.html')

def nutrition(request):
    # if request.method == 'POST':
    # response = requests.get('https://api.covid19api.com/countries').json()
    my_json=open('media/data/foods.json','r')
    jsondata=my_json.read()
    obj=json.loads(jsondata)
    count=len(obj)
    # return render(request, 'nutrica/nutrition.html',{'response':response, 'num':num})
    # name = request.POST.get('food_name')
    # food_name = obj[name]
    # for i in range(count):
    #     if(str(obj[i]['name'])==name):
    #         food_name = obj[i]
    #         item = obj[i]
    if request.method == "POST":
        item_name = request.POST.get('food_name')
        if(item_name == "none"):
            messages.error(request, "Please select an item")
            return redirect('nutrition')
        nutientsItem = []
        sum = 0
        for i in range(count):
            if(str(obj[i]['name'])==item_name):
                item = obj[i]
                nutrientsdata = obj[i]['nutrients']
                for j in nutrientsdata:
                    nutientsItem.append(j)
                for j in nutientsItem:
                    sum = sum + nutrientsdata[j]

                    # sum1 = j.Calcium + j.Iron + j.Potassium + j.Magnesium + j.Phosphorus + j.Sodium +
            # if(str(obj[i]['name'])==item_name):
                # nutrientsdata = obj[i]['nutrients']
        sum = float("{:.2f}".format(sum/100))
        return render(request, 'nutrica/nutrition.html', {'obj':obj, 'item': item, 'count':count, "nutrientsdata": nutrientsdata, "nutientsItem":nutientsItem, "sum": sum})
    else:
        return render(request, 'nutrica/nutrition.html',{'obj':obj, count:'count'})



def myaccount(request):
    jsonFile = open('media/data/BrowserHistory1.json','r',encoding="utf8").read()
    objData = json.loads(jsonFile)
    obj = objData['Browser History']
    if request.method == "GET":
        return render(request, 'nutrica/myaccount.html', context={'obj': obj})
    else:
        return render(request, 'nutrica/myaccount.html')




def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        connection_way = request.POST['connection_way']
        day_time = request.POST['day_time']
        # send_mail(
        #     name, 
        #     message,
        #     phone,
        #     email,
        #     ['vikramnegi175@gmail.com'],
        # )
        if name and email and phone and message and connection_way and day_time:
                return render(request,'nutrica/appointmentStatus.html', context={
                'name':name,
                'email' : email,
                'phone' : phone,
                'message' :message,
                'connection_way' : connection_way,
                'day_time' : day_time
            })
        else:
            messages.error(request, 'Please Fill all necessary details')
            return redirect('appointment')
    else:
        return render(request, 'nutrica/appointment.html')

@login_required(login_url='login')
def patient(request):
    patient_list = patientdb.objects.all()
    return render(request, 'nutrica/patient.html', context={"patient_list":patient_list, 'num_patient':len(patient_list)})

@login_required(login_url='login')
def singlepatient(request, patient_id):
    patient = patientdb.objects.filter(id=patient_id).get()
    patient = get_object_or_404(patientdb, id=patient_id)
    return render(request, 'nutrica/singlepatient.html', context={
        "patient":patient
    })


# Create your views here.
def index(request):
    # response=requests.get('https://priaid-symptom-checker-v1.p.rapidapi.com').json()
    # return render(request,'nutrica/index.html',{'response':response})



    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    querystring = {"query":"pasta","cuisine":"italian","excludeCuisine":"greek","diet":"vegetarian","maxVitaminB1":"1000","minPotassium":"0","minIron":"0","maxVitaminB5":"1000","minCalcium":"0","minFolicAcid":"0","maxSugar":"1000","limitLicense":"false","maxVitaminB2":"1000","maxVitaminB6":"1000","maxSodium":"1000","minFolate":"0","minVitaminK":"0","minFluoride":"0","maxVitaminB12":"1000","instructionsRequired":"false","maxVitaminA":"5000","ranking":"2","addRecipeInformation":"false","number":"10","minZinc":"0","maxVitaminK":"1000","maxMagnesium":"1000","offset":"0","maxManganese":"1000","maxFluoride":"1000","maxSelenium":"1000","minProtein":"5","minAlcohol":"0","minCalories":"150","minCholine":"0","maxIodine":"1000","maxCopper":"1000","minFat":"5","minVitaminD":"0","maxCholine":"1000","excludeIngredients":"coconut, mango","maxIron":"1000","maxCholesterol":"1000","minSelenium":"0","minVitaminB1":"0","minVitaminB6":"0","maxPotassium":"1000","intolerances":"peanut, shellfish","maxFat":"100","minVitaminC":"0","includeIngredients":"onions, lettuce, tomato","author":"null","maxPhosphorus":"1000","maxFolate":"1000","minMagnesium":"0","maxCaffeine":"1000","minSaturatedFat":"0","maxVitaminE":"1000","minSodium":"0","maxVitaminC":"1000","minVitaminA":"0","minVitaminB3":"0","type":"main course","maxSaturatedFat":"50","minCholesterol":"0","fillIngredients":"false","minFiber":"0","maxCarbs":"100","minVitaminB12":"0","maxAlcohol":"1000","maxCalories":"1500","maxCalcium":"1000","maxZinc":"1000","minPhosphorus":"0","maxVitaminB3":"1000","minVitaminE":"0","maxVitaminD":"1000","maxProtein":"100","minCarbs":"5","maxFiber":"1000","minCopper":"0","minCaffeine":"0","minVitaminB5":"0","minManganese":"0","minSugar":"0","minIodine":"0","minVitaminB2":"0","maxFolicAcid":"1000","equipment":"pan"}

    headers = {
	    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "ef13304a68mshc7c6802e8d8a1e1p1b36cejsn785a1d695c36"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    return render(request,'nutrica/index.html',{'response':response})
    # print(response.text)