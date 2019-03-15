from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Purchase


def addPurchase(request):
    return render(request, 'purchase/purchase_add.html')

def viewPurchase(request):
    context = {
        'buys': Purchase.objects.all()
    }
    return render(request, 'purchase/purchase_view.html', context)