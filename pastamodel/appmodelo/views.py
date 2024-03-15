from django.shortcuts import render
from appmodelo.models import Cliente

def index(request):
    lista_clientes = Cliente.objects.all()
    return render(request, 'appmodelo/index.html', {'clientes':lista_itens})
    


if request.method == 'POST':
    name = request.POST.get('name')
    idade = request.POST.get('idade')
    email = request.POST.get('email')
    telefone= request.POST.get('telefone')
    endereco = request.POST.get('endereco')