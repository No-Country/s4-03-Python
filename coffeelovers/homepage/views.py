from django.shortcuts import render

def home(request):
    context = 'Hola desde views'
    return render(request, 'homepage/home.html', {'context':context})