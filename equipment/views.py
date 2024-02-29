from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ItemList
from .forms import UserRegisterForm, ItemForm, ItemListForm, ShareListForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'equipment/register.html', {'form': form})

@login_required
def list_view(request):
    lists = ItemList.objects.filter(owner=request.user)
    return render(request, 'equipment/list_view.html', {'lists': lists})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('list_view')
    else:
        form = ItemForm()
    return render(request, 'equipment/add_item.html', {'form': form})

@login_required
def create_list(request):
    if request.method == 'POST':
        form = ItemListForm(request.POST)
        if form.is_valid():
            item_list = form.save(commit=False)
            item_list.owner = request.user
            item_list.save()
            return redirect('list_view')
    else:
        form = ItemListForm()
    return render(request, 'equipment/create_list.html', {'form': form})

@login_required
def list_details(request, pk):
    item_list = get_object_or_404(ItemList, pk=pk, owner=request.user)
    items = item_list.items.all()
    shared_with = item_list.shared_with.all()
    return render(request, 'equipment/list_details.html', {'list': item_list, 'items': items, 'shared_with': shared_with})

@login_required
def share_list(request, pk):
    item_list = get_object_or_404(ItemList, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ShareListForm(request.POST, instance=item_list)
        if form.is_valid():
            form.save()
            return redirect('list_details', pk=pk)
    else:
        form = ShareListForm(instance=item_list)
    return render(request, 'equipment/share_list.html', {'form': form, 'list': item_list})

