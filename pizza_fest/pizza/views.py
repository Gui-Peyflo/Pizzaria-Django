from django.shortcuts import render, redirect
from .forms import enderecoForm, usuarioForm
from .models import Endereco, Usuario, Bebida, Pizza, Borda, pedidosF

data = {}


def home(request):
    return render(request, 'pizza/index.html', data)

def endForm(request):
    form = enderecoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_logarc')
    data['formE'] = form
    return render(request, "pizza/cadastro.html", data)


def cadForm(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_login')
    data['formC'] = form
    return render(request, "pizza/cadastrof.html", data)


def logout(request):
    data['acesso'] = False
    data['feito'] = False
    data['erro'] = False

    return render(request, 'pizza/index.html', data)


def login(request):
    if request.POST:
        nome = request.POST["data1"]
        senha = request.POST["data2"]
        dado = Usuario.objects.all()

        for dados in dado:
            if dados.nome == nome and dados.senha == senha:
                print("passou")
                data['acesso'] = True
                data['nome'] = nome
                data['senha'] = senha
                data['end'] = str(dados.idEndereco)
                data['id'] = dados.idUsuario
                pedido_user = pedidosF.objects.filter(id_PedUse=data['id']).all()
                data['pedidos'] = pedido_user
                #data['userEnd'] = dados.idEndereco
                return render(request, 'pizza/login.html', data)
        data['erro'] = True
        return render(request, 'pizza/login.html',data)
    print("não passou")
    return render(request, "pizza/login.html", data)


def ospedidos(request):
    if request.POST:
        formP = pedidosF(
            id_PedUse=data['id'],
            Nome_cliente=data['nome'],
            Nome_Pizza=data['nomeP'],
            Borda=data['bordaSel'],
            Bebida=data['bebidaSel'],
            endereco=data['enderecoC'],
            nBebidas=data['qtdbebidas'],
            nPizza=data['qtdpizzas'],
            entrega="Em andamento",
            preco=data['preco']
        )
        formP.save()
        data['acesso'] = True
        data['feito'] = True
        pedido_user = pedidosF.objects.filter(id_PedUse=data['id']).all()
        data['pedidos'] = pedido_user
        return redirect("url_feitos")

    return render(request, "pizza/ospedidos.html", data)


def pedidosFeitos(request):
    return render(request, "pizza/pedidosFeitos.html", data)


def pedidos(request):
    data["pizzas"] = Pizza.objects.all()
    data["bebidas"] = Bebida.objects.all()
    data["bordas"] = Borda.objects.all()
    valor = 20
    if request.POST:
        nbeb = int(request.POST['nBeb'])
        npiz = int(request.POST['npiz'])
        formSel = request.POST['pizza']
        if formSel == "1":
            nPizza = "Pizza de Calabresa"
        elif formSel == "2":
            nPizza = "Pizza de Alho Óleo"
        elif formSel == "3":
            nPizza = "Pizza de Bacon"
        elif formSel == "4":
            nPizza = "Pizza de Brócolis"
        elif formSel == "5":
            nPizza = "Pizza de Camarão com Queijo"
        elif formSel == "6":
            nPizza = "Pizza de Chocolate"
        elif formSel == "7":
            nPizza = "Pizza de Chocolate Branco"
        elif formSel == "8":
            nPizza = "Pizza de Chocolate Branco com M&Ms"
        elif formSel == "9":
            nPizza = "Pizza de Coração de Galinha"
        elif formSel == "10":
            nPizza = "Pizza de Filé com Cheddar"
        elif formSel == "11":
            nPizza = "Pizza de Frango com Catupiry"
        elif formSel == "12":
            nPizza = "Pizza de Lombo com Catupiry"
        elif formSel == "13":
            nPizza = "Pizza de Marguerita"
        elif formSel == "14":
            nPizza = "Pizza de Chocolate com M&Ms"
        elif formSel == "15":
            nPizza = "Pizza de Mussarela"
        elif formSel == "16":
            nPizza = "Pizza Portuguesa"
        elif formSel == "17":
            nPizza = "Pizza de Quatro Queijos"
        elif formSel == "18":
            nPizza = "Pizza Vegetariana"

        print(nPizza)
        selectBebi = request.POST["bebida"]
        print(selectBebi)
        selectBorda = request.POST["bordas"]
        print(selectBorda)

        if npiz != 0:
            valor = valor * npiz
        else:
            npiz = 1
        if selectBebi != "Sem Bebida":
            if nbeb != 0:
                valor += 5 * nbeb
            else:
                valor += 5
                nbeb = 1
        if selectBorda != "Sem Borda":
            valor += 5*npiz

        data['preco'] = valor
        data['nomeP'] = nPizza
        data['bordaSel'] = selectBorda
        data["bebidaSel"] = selectBebi
        data["status"] = "Em Andamento"
        data["enderecoC"] = data["end"]
        data["acesso"] = data["acesso"]
        data['qtdbebidas'] = nbeb
        data['qtdpizzas'] = npiz
        data['feito'] = True
        return redirect('url_ospedidos')
    return render(request, 'pizza/pedidos.html', data)




