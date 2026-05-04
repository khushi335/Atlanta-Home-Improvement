from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"main/index.html")
    
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def areas_we_serve(request):
    return render(request, 'main/areas_we_serve.html')

# Service Views
def services_home(request):
    return render(request, 'main/all_services.html')

def bathroom_remodeling(request):
    return render(request, 'main/bathroom.html')

def kitchen_remodeling(request):
    return render(request, 'main/kitchen.html')

def basement_finishing(request):
    return render(request, 'main/basement.html')

def home_additions(request):
    return render(request, 'main/additions.html')