from django.db import models


# Create your models here.

class Endereco(models.Model):
    idEndereco = models.AutoField(primary_key=True, blank=False)
    logradouro = models.CharField(max_length=30, null=False, blank=False)
    endereco = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=45, null=False, blank=False)
    municipio = models.CharField(max_length=45, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    numero = models.IntegerField()

    def __str__(self):
        return self.logradouro + " " + self.endereco + ", " + str(self.numero)


class Bebida(models.Model):
    idBebida = models.AutoField(primary_key=True, blank=False)
    nome = models.CharField(max_length=45, null=False, blank=False)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    tamanho = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.nome


class Borda(models.Model):
    idBorda = models.AutoField(primary_key=True, blank=False)
    tipo_Borda = models.CharField(max_length=45, null=False, blank=False, verbose_name="Tipo da Borda")
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tipo_Borda

class Pizza(models.Model):
    idPizza = models.AutoField(primary_key=True, blank=False)
    recheio = models.CharField(max_length=45, null=False, blank=True)
    valor = models.DecimalField(max_digits= 6, decimal_places=2)
    tamanho = models.CharField(max_length=1, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=True)
    foto = models.FileField(upload_to="media/")
    idBorda = models.ForeignKey(Borda, on_delete=models.CASCADE, null=True)

    @property
    def valor_pizza(self):
        total = 0
        total += self.valor
        total += self.idBorda.valor
        return total

    def __str__(self):
        return self.recheio





class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, blank=False)
    nome = models.CharField(max_length=45, null=False, blank=False)
    senha = models.CharField(max_length=24, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    email = models.EmailField(max_length=45, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    isFunc = models.BooleanField(default=True, null=False, blank=False)
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True, blank=False)
    status = models.CharField(max_length=25, null=False, blank=True)
    total_pedido = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPedido)


class Produto_Pedido(models.Model):
    idProduto_Pedido = models.AutoField(primary_key=True, blank=False)
    quantidade_Pizza = models.IntegerField()
    quantidade_Bebida = models.IntegerField()
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idBebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    idPizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idProduto_Pedido)


class pedidosF(models.Model):
    id_pedidos = models.AutoField(primary_key=True, blank=False,null=False)
    id_PedUse = models.IntegerField(default=1)
    Nome_cliente = models.CharField(max_length=50, null=False)
    Nome_Pizza = models.CharField(max_length=50, null=False)
    Borda = models.CharField(max_length=20, null=False)
    Bebida = models.CharField(max_length=20, null=False)
    endereco = models.CharField(max_length=40, null=False)
    nBebidas = models.IntegerField(default=0)
    nPizza = models.IntegerField(default=1)
    entrega = models.CharField(max_length=40, null=False)
    preco = models.DecimalField(max_digits=6,  decimal_places=2, null=False, default=20)

    def __str__(self):
        return self.Nome_cliente


