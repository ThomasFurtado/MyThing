from django.shortcuts import render, redirect
from .models import Choice
from .forms import AddForm

def home_screen_view(request):
    pratos = Choice.objects.all()
    form = AddForm()
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'pratos': pratos}
    context['form'] = form
    return render(request, 'pratos/home.html', context)

def delete(request, pk):
    item = Choice.objects.get(id=pk)

    if request.POST:
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'pratos/delete.html', context)

