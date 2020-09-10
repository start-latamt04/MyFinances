from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from django.shortcuts import *
from .models import Saldo
from .forms import UserForm, SaldoForm


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
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            Saldo.objects.create(saldo=0, meta=0, gastos=0, total_gastos=0, user=request.user).save()
            return redirect('accounts:page-one')
    else:
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
            messages.error(request, 'Usuario ou senha incorreto!')
            return redirect('accounts:user_login')
    return render(request, template_name)


def index(request):
    template_name = 'index.html'
    if request.user.is_authenticated:
        return redirect('accounts:page-one')
    return render(request, template_name)


@login_required(login_url='/login/')
def relatorio(request):
    if request.method == 'POST':
        month = request.POST.get('meses')
        year = request.POST.get('year')
        total = Saldo.objects.filter(user_id=request.user.id, created_at__month=month, created_at__year=year)
    else:
        data = datetime.now()
        mes = data.month
        ano = data.year
        total = Saldo.objects.filter(user_id=request.user.id, created_at__month=mes, created_at__year=ano)
    data = datetime.now()
    dia = data.strftime("%d")
    if str(dia) == '01':
        Saldo.objects.filter(user_id=request.user.id).update(saldo=0, meta=0, descricao='', gastos=0, total_gastos=0)

    res = Saldo.objects.get(user_id=request.user.id)
    context = {
        'total': total,
        'res': res,
        'dia': dia,
    }
    template_name = 'relatorio_despesas.html'
    return render(request, template_name, context)


@login_required(login_url='/login/')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Você saiu do sistema.')
        return redirect('accounts:index')
    else:
        messages.error(request, 'Você precisa estar logado!')
        return redirect('accounts:user_login')


@login_required(login_url='/login/')
def page_one(request):
    saldo = get_object_or_404(Saldo, user_id=request.user.id)
    form = SaldoForm(instance=saldo)
    template_name = 'page-one.html'

    if request.method == 'POST':
        form = SaldoForm(request.POST, instance=saldo)
        if form.is_valid():
            saldo = form.save(commit=False)
            saldo.saldo = form.cleaned_data['saldo']
            saldo.meta = form.cleaned_data['meta']
            saldo.gastos = form.cleaned_data['gastos']
            saldo.descricao = form.cleaned_data['descricao']
            saldo.save()
            Saldo.objects.filter(user_id=request.user.id).update(saldo=F('saldo') - F('gastos'))
            Saldo.objects.filter(user_id=request.user.id).update(total_gastos=F('total_gastos') + F('gastos'))
            return redirect('accounts:page-one')
    return render(request, template_name, {'form': form})
