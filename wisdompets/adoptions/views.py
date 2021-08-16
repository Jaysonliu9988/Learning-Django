from django.shortcuts import render
from django.http import Http404

from .models import Pet


def home(request):  # home page => localhost:8000
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
    })
def pet_detail(request, pet_id):
    try:
         pet = Pet.objects.get(id=pet_id) # localhost:8000/adoptions/1/
    except Pet.DoesNotExist:
        raise Http404('pet not found')  # 404 page => localhost:8000/adoptions/9999
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })