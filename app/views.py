from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Loading my model
import keras
from keras.models import load_model
model = keras.models.load_model("C:\\Users\\hp\\OneDrive\\Desktop\\Life Exepctancy Enhancer W\\app\\model prediction life expectency ultimate accuracy .h5")


@login_required(login_url='login')
# Create your views here.


# with open(os.path.join(settings.STATICFILES_DIRS[0], 'model prediction life expectency ultimate accuracy .h5'), 'rb') as f:
#     model = keras.models.load_model(f)

def LoginPage(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print("Username:", username)
        print("Password:", pass1)
        user = authenticate(request, username=username, password=pass1)
        print("User:", user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request, 'login.html')

def SignupPage(request):
    if(request.method == "POST"):
        uname =  request.POST.get('username')
        email =  request.POST.get('email')
        pass1 =  request.POST.get('password1')
        pass2 =  request.POST.get('password2')
        my_user = User.objects.create_user(uname,email,pass1)

        if(pass1 != pass2):
            return HttpResponse("Your passwords do not match")
        my_user.save()
        print(uname,email,pass1,pass2)

        return redirect('login')
    
    return render (request,"signup.html")


def HomePage(request):
    print("I tried boss")
    if request.method == 'POST':
        print("I tried boss. Reached inside POST")
        gender =  request.POST.get('gender')
        age =  request.POST.get('Age')
        weight =  request.POST.get('Weight')
        height =  request.POST.get('Height')
        marital_status =  request.POST.get('MaritalStatus')
        annual_income =  request.POST.get('AnnualIncome')
        general_health =  request.POST.get('fitness')
        exercise =  int(request.POST.get("Exercise"))
        diabetic =  request.POST.get('diabetic')
        alcohol =  int(request.POST.get('Alcohol'))
        smoking =  request.POST.get('smoking')
        domestic_environment =  request.POST.get('DomesticEnvironment')
        medication_consumption =  request.POST.get('MedicineConsumption')
        nutrition =  request.POST.get('Nutrition')
        social_life =  request.POST.get('SocialLife')
        sleep_schedule =  request.POST.get('SleepSchedule')
        chronic_mental_health =  request.POST.get('ChronicMentalHealth')

        print(gender,age,weight,height,marital_status,annual_income,general_health,exercise,diabetic,alcohol,smoking,domestic_environment,medication_consumption,nutrition,social_life,sleep_schedule,chronic_mental_health)
        print("Marital Status",marital_status)

# Creating arrays for great, fair and poor performing areas
        great_performing_areas = []
        fair_performing_areas = []
        poor_performing_areas = []

        # Transforming the recieved data in a format that model can interpret
        user_input_array = []
        # Age / Current Age
        user_input_array.append(int(age))
       # Height
        user_input_array.append(int(height)) 
       # weight
        user_input_array.append(int(weight))   
        # Gender
        if(gender == "male"):
            user_input_array.append(1)
        else:
            user_input_array.append(0)  
        # Annual Income /Financial Situation  (Static for now)
        '''
        0: 1-3
        1: 3-5
        2: 5-8
        3: 8-15
        4: 15 above
        '''
        annual_income = int(annual_income)
        if(annual_income >= 1 and annual_income <=3):
            user_input_array.append(0)
        elif(annual_income >=3 and annual_income <= 5):
            user_input_array.append(1)
        elif(annual_income >=5 and annual_income <= 8):
            user_input_array.append(2)
        elif(annual_income >=8 and annual_income <= 15):
            user_input_array.append(3)
        elif(annual_income > 15):
            user_input_array.append(4)

       # Fitness / Workout  (Static for now)
        if(exercise == 0):
            user_input_array.append(0)
            poor_performing_areas.append("Exercise")
        elif(exercise == 1 or exercise == 2):
            user_input_array.append(1)
            fair_performing_areas.append("Exercise")
        elif(exercise == 3 or exercise == 4):
            user_input_array.append(2)
            great_performing_areas.append("Exercise")
        elif(exercise == 5 or exercise == 6):
            user_input_array.append(3)
            great_performing_areas.append("Exercise")
        elif(exercise == 7):
            user_input_array.append(4)
            great_performing_areas.append("Exercise")
        else:
            user_input_array.append(3)

        # General Health 
        if(general_health == "poor"):
            user_input_array.append(0)
            poor_performing_areas.append("General Health")
        elif(general_health == "fair"):
            user_input_array.append(1)
            fair_performing_areas.append("General Health")
        elif(general_health == "good"):
            user_input_array.append(2)
            great_performing_areas.append("General Health")
        elif(general_health == "VeryGood"):
            great_performing_areas.append("General Health")
            user_input_array.append(3)  
        elif(general_health == "excellent"):
            great_performing_areas.append("General Health")
            user_input_array.append(4)     
        else:
            user_input_array.append(3)
        #  Alcohol   (Static for now)
        if(alcohol <= 12 and alcohol >= 5):
            user_input_array.append(0)
            poor_performing_areas.append("Alcohol Consumption")
        elif(alcohol > 3 and alcohol < 5):
            user_input_array.append(1)
            poor_performing_areas.append("Alcohol Consumption")
        elif(alcohol >= 2 and alcohol <= 3):
            user_input_array.append(2)
            fair_performing_areas.append("Alcohol Consumption")
        elif(alcohol == 1):
            user_input_array.append(1)
            great_performing_areas.append("Alcohol Consumption")
        elif(alcohol == 0):
            user_input_array.append(0)
            great_performing_areas.append("Alcohol Consumption")


        # Smoking  (Static for now)
        if(smoking == "StillMoreThanOnePack"):
            user_input_array.append(0)
            poor_performing_areas.append("Smoking")
        elif(smoking == "StillOnePack"):
            user_input_array.append(1)
            poor_performing_areas.append("Smoking")
        elif(smoking == "StillHalfPackOrLess"):
            user_input_array.append(2)
            poor_performing_areas.append("Smoking")
        elif(smoking == "QuitGreaterThan10YearAgo"):
            user_input_array.append(5)
            great_performing_areas.append("Smoking")
        elif(smoking == "quit_one_two_nine_year_ago"):
            user_input_array.append(4)     
            great_performing_areas.append("Smoking")
        elif(smoking == "quit_less_than_one_year_ago"):
            user_input_array.append(3)        
            great_performing_areas.append("Smoking")
        elif(smoking == "never"):
            user_input_array.append(6)           
            great_performing_areas.append("Smoking")
         

        # Marital Status

        # Married, never married, divorced
        if(marital_status == "married"):
            user_input_array.append(1)
            user_input_array.append(0)
            user_input_array.append(0)

        elif(marital_status == "not_married"):
            user_input_array.append(0)
            user_input_array.append(1)
            user_input_array.append(0)
        elif(marital_status == "divorced"):
            user_input_array.append(0)
            user_input_array.append(0)
            user_input_array.append(1) 
        elif(marital_status == "prefer_not_to_say"):
            user_input_array.append(0)
            user_input_array.append(0)
            user_input_array.append(0)  
        else:
            user_input_array.append(0)
            user_input_array.append(0)
            user_input_array.append(0)             

        # Diabetic
        if(diabetic == "Yes"):
            user_input_array.append(0)
        else:
            user_input_array.append(1)

        # Nutrition
        if(nutrition == "JunkFoodAddict"):
            user_input_array.append(0)
            poor_performing_areas.append("Nutrition")
        elif(nutrition == "HealthyForTheMostPart"):
            user_input_array.append(1)
            great_performing_areas.append("Nutrition")
        elif(nutrition == "OnlyOnSelectedDates"):
            user_input_array.append(2)
            great_performing_areas.append("Nutrition")
        elif(nutrition == "NoJunkFood"):
            user_input_array.append(3)
            great_performing_areas.append("Nutrition")
        else:
            user_input_array.append(3)


        # Social Life
        if(social_life == "None"):
                user_input_array.append(0)
                poor_performing_areas.append("Social Life")
        elif(social_life == "Barely"):
            user_input_array.append(1)
            poor_performing_areas.append("Social Life")
        elif(social_life == "Healthy"):
            user_input_array.append(2) 
            great_performing_areas.append("Social Life")
        elif(social_life == "ManyCloseFriends"):
            user_input_array.append(3)
            great_performing_areas.append("Social Life")
        else:
            user_input_array.append(3)

        #chronic_mental_health
        if(chronic_mental_health == "Depressed-Pessimistic"):
                user_input_array.append(0)
                poor_performing_areas.append("Mental Health")
        elif(chronic_mental_health == "Stressed-Worried"):
            user_input_array.append(1)
            poor_performing_areas.append("Mental Health")
        elif(chronic_mental_health == "Complex"):
            user_input_array.append(2) 
            fair_performing_areas.append("Mental Health")
        elif(chronic_mental_health == "Positive"):
            user_input_array.append(3)  
            great_performing_areas.append("Mental Health")
        elif(chronic_mental_health == "Calm"):
            user_input_array.append(4)           
            great_performing_areas.append("Mental Health")
        else:
            user_input_array.append(4)

       #Domestic Environment
        if(domestic_environment == "QuiteToxic"):
                user_input_array.append(0)
                poor_performing_areas.append("Domestic Environment")
        elif(domestic_environment == "PreferNotToSayDomesticEnvironment"):
            user_input_array.append(1)
        elif(domestic_environment == "HealthyVibes"):
            user_input_array.append(2) 
            poor_performing_areas.append("Domestic Environment")    
        elif(domestic_environment == "Peaceful"):
            poor_performing_areas.append("Domestic Environment")
            user_input_array.append(3)    
        elif(domestic_environment == "Uplifting"):
            great_performing_areas.append("Domestic Environment")
            user_input_array.append(4)   
        else:
            user_input_array.append(4)

        # Sleep Schedule (not actually using to predict)   
        print("Great Performing areas: ",great_performing_areas)
        print("fair Performing areas: ",fair_performing_areas) 
        print("poor Performing areas: ",poor_performing_areas) 

        # Plottings 


        df = pd.read_excel("C:\\Users\\hp\\OneDrive\\Desktop\\Life Exepctancy Enhancer W\\User Data\\user1.xlsx")
        plot_save_dir = 'C:\\Users\\hp\\OneDrive\\Desktop\\Life Exepctancy Enhancer W\\app\\static\\Plottings'

        # General Health vs Week
        plt.figure()
        sns.set_style('darkgrid')
        health_counts = df['general_health'].value_counts()
        plt.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90)
        plt.rcParams['font.size'] = 16
        plt.title("General Health")
        plt.axis('equal')  # Make the pie chart a perfect circle
        plt.savefig(plot_save_dir + "\\general_health.jpg", format='jpg')

        # Alcohol vs Week
        plt.figure()
        sns.set_style('darkgrid')
        sns.countplot(x='Alcohol', data=df)
        plt.rcParams['font.size'] = 16
        plt.savefig(plot_save_dir + "\\Alcohol.jpg", format='jpg')

        # Workout/ Exercise
        plt.figure(figsize=(14,10))
        health_counts = df['Workout'].value_counts()
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False,         wedgeprops=dict        (width=0.5, edgecolor='w'))
        ax.set_aspect('equal')
        centre_circle = plt.Circle((10,0),0.20,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.tight_layout()
        plt.title("Exercise")
        plt.rcParams['font.size'] = 16
        plt.savefig(plot_save_dir + "\\Workout.jpg", format='jpg')

        # Smoking vs Week
        plt.figure(figsize=(10,5))
        sns.set_style('darkgrid')
        sns.lineplot(x='Week', y='Smoking', data=df, color = "red")
        plt.xlabel('Week')
        plt.ylabel('Smoking')
        plt.title('Smoking vs Week')
        plt.rcParams['font.size'] = 16
        plt.savefig(plot_save_dir + "\\Smoking.jpg", format='jpg')
        
        # Mental Health
        plt.figure()
        sns.set_style('darkgrid')        
        health_counts = df['chronic_mental_health'].value_counts()
        plt.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90)
        plt.rcParams['font.size'] = 16
        plt.axis('equal')  # Make the pie chart a perfect circle
        plt.title("Mental Health")
        plt.savefig(plot_save_dir + "\\Mental Health.jpg", format='jpg')        

        # Nutrition
        plt.figure(figsize=(35,8))
        health_counts = df['Nutrition'].value_counts()
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        ax.pie(health_counts, labels=health_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops=dict(width=0.3, edgecolor='w'))
        ax.set_aspect('equal')
        centre_circle = plt.Circle((10,0),0.10,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.tight_layout()
        plt.rcParams['font.size'] = 16
        plt.title("Nutrition")
        plt.savefig(plot_save_dir + "\\Nutrition.jpg", format='jpg') 

        # Social Life
        plt.figure(figsize=(10,5))
        sns.set_style('darkgrid')
        sns.lineplot(x='Week', y='Social Life', data=df, color = "green")
        plt.xlabel('Week')
        plt.ylabel('Social Life')
        plt.title('Social Life vs Week')
        plt.savefig(plot_save_dir + "\\Social Life.jpg", format='jpg') 


        context = {'great_performing_areas': great_performing_areas, 'fair_performing_areas': fair_performing_areas, 'poor_performing_areas': poor_performing_areas}

        print("Here is the final array -> ", user_input_array)
        prediction = model.predict([user_input_array])
        print(prediction)


        return render(request,"output_page.html", {'prediction': round(prediction[0][0]),'prediction_max': round(prediction[0][0] + 4),"Performance":context})
    

    return render(request,"home.html")

def OutputPage(request):
    return render(request,"output_page.html")