from django.shortcuts import render, redirect
from account.models import User
from .models import Card
from django.contrib.auth.decorators import login_required

def get_all(request):
    cards = Card.objects.filter(user=request.user)

    return render(request, 'card/get_all.html', {
        "cards":cards
    })

@login_required
def get(request, pk):
    card = Card.objects.filter(user=request.user).get(pk=pk)

    return render(request, 'card/get.html', {
        'card':card
    })

@login_required
def add(request):
    if request.method == 'POST':
        description = request.POST.get('description', '')
        link = request.POST.get('link', '')

        if link:
            Card.objects.create(description=description, link=link, user=request.user)

            return redirect('/')
        
    return render(request, 'card/add.html')

    
