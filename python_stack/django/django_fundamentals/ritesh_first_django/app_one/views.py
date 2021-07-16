from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def hello_name(request, name):
    context = {
        "htmlname": name,
        "namelist": ["Dumbo","Dofus","Maximus","Rees"]
    }
    return render(request, "helloname.html", context)