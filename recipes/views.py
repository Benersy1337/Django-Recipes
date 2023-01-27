from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luan Roberto',
    })