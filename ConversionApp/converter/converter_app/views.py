from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def testInputs(value1, value2, num1):
    #This block of code converts the number from the user to meters.
    num1InMeters = 0
    if value1 == 'me': #meters
        num1InMeters = float(num1)
    elif value1 == 'mm': #millimeters
        num1InMeters = float(num1) / 1000
    elif value1 == 'cm': #centimeters
        num1InMeters = float(num1) / 100
    elif value1 == 'de': # decimeters
        num1InMeters = float(num1) / 10
    elif value1 == 'dam': #dekameter
        num1InMeters = float(num1) / 0.1
    elif value1 == 'hm': #hectometer
        num1InMeters = float(num1) / 0.01
    elif value1 == 'km': # kilometer
        num1InMeters = float(num1) / 0.001
    elif value1 == 'in': # inches
        num1InMeters = float(num1) / 39.37
    elif value1 == 'ft': # feet
        num1InMeters = float(num1) / 3.281
    elif value1 == 'ya': # yards
        num1InMeters = float(num1) / 1.094
    elif value1 == 'mi': # miles
        num1InMeters = float(num1) * 1609
    elif value1 == 'nami': #nautical miles
        num1InMeters = float(num1) * 1852
    elif value1 == 'league': # league
        num1InMeters = float(num1) * 5556

    solution = 0

    #This code converts from meters to value 2
    if value2 == 'me':
        solution = num1InMeters
    elif value2 == 'mm': #millimeters
        solution = num1InMeters * 1000
    elif value2 == 'cm': #centimeters
        solution = num1InMeters * 100
    elif value2 == 'de': # decimeters
        solution = num1InMeters * 10
    elif value2 == 'dam': #dekameter
        solution = num1InMeters / 10
    elif value2 == 'hm': #hectometer
        solution = num1InMeters / 100
    elif value2 == 'km': # kilometer
        solution = num1InMeters / 1000
    elif value2 == 'in': # inches
        solution = num1InMeters * 39.37
    elif value2 == 'ft': # feet
        solution = num1InMeters * 3.281
    elif value2 == 'ya': # yards
        solution = num1InMeters * 1.094
    elif value2 == 'mi': # miles
        solution = num1InMeters / 1609
    elif value2 == 'nami': #nautical miles
        solution = num1InMeters / 1852
    elif value2 == 'league': # league
        solution = num1InMeters / 5556

    return solution

## test user answer against the right answer and return a bool
def testAnswer(userAnswer, type1, type2, val):
    # pull right answer into variable using testInputs
    rightAnswer = testInputs(type1, type2, val)
    # compair user answer to right answer
    isCorrect = (userAnswer == rightAnswer)
    return isCorrect

    # This block of code converts from meters to the specified unit


# Create your views here.
def converter(request):
    print("Hi Tyler!")
    return render(request, 'home.html',{'name': 'Olivia'})
    
def base(request):
    return render(request, 'base.html')

def testme(request):
    #this gets values from the testme page, the units, the number being converted and the user's answer
    type1 = request.GET['type1', 'me']
    type2 = request.GET['type2', 'me']
    num1 = request.GET['num1', 1]
    userAnswer = request.GET['userAnswer', 1]

    isCorrect = testAnswer(userAnswer, type1, type2, num1)
    values= {'result': isCorrect}
    
    return render(request, 'test_me.html', values)

def convert(request):
    return render(request, 'converter.html')

def converter(request):
    print("Hi Poya!")
    return render(request, 'converter.html', {'name': 'Olivia'})

def add(request):
       
    value1 = request.GET.get('type1')
    value2 = request.GET.get('type2')
    print("hi")
    num1 = request.GET.get('num1')
    

    print(request.GET, request.method)
   
    solution = testInputs(value1, value2, num1)
    values= {'res': solution}
    
    
    return render(request,'converter.html', values)


class TestMeView(TemplateView):
    template_name='test_me.html'