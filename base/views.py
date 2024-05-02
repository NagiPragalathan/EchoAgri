from django.shortcuts import render
from g4f.client import Client

# Create your views here.


def SoilBasedFeedTheSeed(request):
    if request.method == 'POST':
        soil_name = request.POST.get('soilName')
        description = request.POST.get('description')
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "System", "content": "You are a use full ai to give the recommendation by getting soil's name and this description  response in english"},
                {"role": "user", "content": f"the soil name is {soil_name} and the details are {description}. Now give me the Recommendation about the  soil for planting seed."},
                ],
        )
        return render(request, 'Soil_Bades_Feed_The_seed.html', {'soil_name': soil_name, 'description': description, "recommendation": response.choices[0].message.content})
    return render(request, 'Soil_Bades_Feed_The_seed.html')


def weatherBasedFeedTheSeed(request):
    if request.method == 'POST':
        soil_name = request.POST.get('soilName')
        description = request.POST.get('description')
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "System", "content": "You are a use full ai to give the recommendation by getting Weather condition and this description response in english"},
                {"role": "user", "content": f"the Weather condition is {soil_name} and the details are {description}. Now give me the Recommendation about the  Weather for planting seed."},
                ],
        )
        return render(request, 'weatherBasedFeedTheSeed.html', {'soil_name': soil_name, 'description': description, "recommendation": response.choices[0].message.content})
    return render(request, 'weatherBasedFeedTheSeed.html')

def Pricing(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "System", "content": "You are a use full ai to give the cost of the process and budget by given description response in english"},
                {"role": "user", "content": f"the idea is { description } Now give me the cost and budgets about the  given idea."},
                ],
        )
        return render(request, 'Pricing.html', {'description': description, "recommendation": response.choices[0].message.content})
    return render(request, 'Pricing.html')

def home(request):
    return render(request, "index.html")