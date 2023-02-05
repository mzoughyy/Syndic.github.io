from django.shortcuts import render
from django.views import View

class RegisterationView(View):
    def get(self, request):
        return render(request, 'authentification/register.html')