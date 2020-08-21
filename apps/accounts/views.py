from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .forms import *

# Create your views here.


def cadastro(request):
    template_name = 'registro.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('accounts:index')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


def user_login(request):
    template_name = 'user_login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:page-one')
        else:
            print('Deu ruim')

    return render(request, template_name, {})


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {})


@login_required(login_url='/login/')
def relatorio(request):
    template_name = 'relatorio_despesas.html'
    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('accounts:index')


@login_required(login_url='/login/')
def page_one(request):
    template_name = 'page-one.html'
    if request.method == 'POST':
        form = SaldoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:page-one')
    return render(request, template_name, {})
