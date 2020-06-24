from django.shortcuts import render, redirect
from pets.models import petEncontrado
from pets.forms import petEncontradoForm


def list_petEncontrado(request):
    pets = petEncontrado.objects.all()
    return render(request, 'pet.html', {'pets': pets})


def create_petEncontrado(request):
    form = petEncontradoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_petEncontrado')

    return render(request, 'pet-form.html', {'form': form})


def update_petEncontrado(request, id):
    pet = petEncontrado.objects.get(id=id)
    form = petEncontradoForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        return redirect('list_petEncontrado')

    return render(request, 'pet-form.html', {'form': form, 'pet': pet})


def delete_petEncontrado(request, id):
    pet = petEncontrado.objects.get(id=id)

    if request.method == 'POST':
        pet.delete()
        return redirect('list_petEncontrado')

    return render(request, 'pet-delete-confirm.html', {'pet': pet})
