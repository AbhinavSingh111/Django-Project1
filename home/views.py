from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is HOME page")
    context = {
        "variable1" : "This is the variable sent via context from views",
        "variable2" : "This is the second variable coming from template which has been rendered via view"
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("This is ABOUT page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is SERVICES page")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is CONTACTS page")
    return render(request, 'contact.html')