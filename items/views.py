from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import NewItemForm
import os

# Create your views here.
def itemsTest(request):
    items_Display = Item.objects.filter(is_sold = False)[0:6]
    categories_Display = Category.objects.all()
    return render(request, 'items/itemsIndex.html', {
        'items': items_Display,
        'categories': categories_Display,
    })

def newitem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save()
            item.created_by = request.user
            item.save()

            return redirect('item:testTemplate1')
    else:
        form = NewItemForm()
            
    return render(request, 'items/forms.html', {
        'form': form,
        'title': 'New Item',
    })