from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def congo(request):
    return render(request, 'congo.html')

def level1(request):
    return render(request, 'level1.html')
def level2(request):
    return render(request, 'level2.html')
def level3(request):
    return render(request, 'level3.html')
def level4(request):
    return render(request, 'level4.html')
def level5(request):
    return render(request, 'level5.html')
def level6(request):
    return render(request, 'level6.html')