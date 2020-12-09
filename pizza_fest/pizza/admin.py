from django.contrib import admin
from .models import Endereco
from .models import Bebida
from .models import Borda
from .models import Pizza
from .models import Usuario
from .models import Pedido
from .models import Produto_Pedido, pedidosF
#from .models import imagens


# Register your models here.
admin.site.register(Endereco)
admin.site.register(Bebida)
admin.site.register(Borda)
admin.site.register(Pizza)
admin.site.register(Usuario)
admin.site.register(Pedido)
admin.site.register(Produto_Pedido)
admin.site.register(pedidosF)
#admin.site.register(imagens)