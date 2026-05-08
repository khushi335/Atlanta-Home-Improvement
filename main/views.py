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

def bathroom_remodeling(request):
    return render(request, 'main/bathroom.html')

def kitchen_remodeling(request):
    return render(request, 'main/kitchen.html')

def basement_finishing(request):
    return render(request, 'main/basement.html')

def home_additions(request):
    return render(request, 'main/additions.html')
    
def painting(request):
    return render(request, 'main/painting.html')

def home_improvement(request):
    return render(request, 'main/home_improvement.html')

def patios_decks(request):
    return render(request, 'main/patios_decks.html')

def cabinets(request):
    return render(request, 'main/cabinets.html')

def woodworking(request):
    return render(request, 'main/woodworking.html')

def hardscaping(request):
    return render(request, 'main/hardscaping.html')

def walkway_designs(request):
    return render(request, 'main/walkways.html')

def pergolas(request):
    return render(request, 'main/pergolas.html')

def lead_removal(request):
    return render(request, 'main/lead_removal.html')

def shed_builder(request):
    return render(request, 'main/sheds.html')

def lead_renovator(request):
    return render(request, 'main/lead_renovator.html')