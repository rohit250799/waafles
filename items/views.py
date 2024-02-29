from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Item
from .forms import NewItemForm, EditItemForm
import os

# Create your views here.
def itemsIndex(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories_Display = Category.objects.all()
    return render(request, 'items/itemsIndex.html', {
        'items': items,
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

def edititem(request):
    item = get_object_or_404(Item, created_by = request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect
