from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def greeting(request, name):
    return render(request, "greeting.html", {"name":name})

def cube(request, num):
    num2 = num*num*num
    return render(request,"cube.html", {"num2":num2, "num":num})