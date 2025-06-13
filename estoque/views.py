from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Produto, Categoria, MovimentacaoEstoque
from django.contrib.auth.models import User, Group

def is_gerente(user):
    return user.groups.filter(name='Gerentes').exists()

def is_superior(user):
    return user.groups.filter(name='Superiores').exists()

@login_required
def dashboard(request):
    produtos = Produto.objects.all()
    produtos_em_estoque = produtos.filter(quantidade__gt=0)
    produtos_baixo_estoque = produtos.filter(quantidade__lte=5)
    return render(request, 'estoque/dashboard.html', {
        'produtos': produtos,
        'produtos_em_estoque': produtos_em_estoque,
        'produtos_baixo_estoque': produtos_baixo_estoque,
    })

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})

@user_passes_test(is_superior)
def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')

        categoria = get_object_or_404(Categoria, id=categoria_id)
        produto = Produto.objects.create(
            nome=nome,
            descricao=descricao,
            categoria=categoria,
            quantidade=quantidade,
            preco=preco
        )
        messages.success(request, 'Produto adicionado com sucesso!')
        return redirect('lista_produtos')
    
    categorias = Categoria.objects.all()
    return render(request, 'estoque/adicionar_produto.html', {'categorias': categorias})

@login_required
def movimentar_estoque(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade'))
        observacao = request.POST.get('observacao')

        if tipo == 'saida' and quantidade > produto.quantidade:
            messages.error(request, 'Quantidade insuficiente em estoque!')
            return redirect('movimentar_estoque', produto_id=produto_id)

        if tipo == 'saida' and not (is_gerente(request.user) or is_superior(request.user)):
            messages.error(request, 'Você não tem permissão para realizar saídas!')
            return redirect('movimentar_estoque', produto_id=produto_id)

        if tipo == 'entrada' and not (is_gerente(request.user) or is_superior(request.user)):
            messages.error(request, 'Você não tem permissão para realizar entradas!')
            return redirect('movimentar_estoque', produto_id=produto_id)

        MovimentacaoEstoque.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            usuario=request.user,
            observacao=observacao
        )

        if tipo == 'entrada':
            produto.quantidade += quantidade
        else:
            produto.quantidade -= quantidade
        produto.save()

        messages.success(request, 'Movimentação realizada com sucesso!')
        return redirect('lista_produtos')

    return render(request, 'estoque/movimentar_estoque.html', {'produto': produto})

@user_passes_test(is_superior)
def adicionar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Categoria.objects.create(nome=nome, descricao=descricao)
        messages.success(request, 'Categoria adicionada com sucesso!')
        return redirect('dashboard')
    
    return render(request, 'estoque/adicionar_categoria.html')
