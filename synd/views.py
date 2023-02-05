from django.shortcuts import render

def index(request):
    return render(request,'synd/index.html')
def add_synd(request):
    return render(request,'synd/add_synd.html')