import os 
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto

class Utils:

    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))
    
class ProdutoClass:

    @staticmethod
    def cria_produto(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                ncm = Utils.gen_digits(8),
                preco = random() * randint(10, 50),
                estoque = randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)

produtos = (
    'Jack Daniels',
    'Jack Fire',
    'Jack Honey',
    'Black Label',
    'Red Label',
    'Blue Label',
    'Bucchanas',
    'Dada',
    'Esteban Martinez',
    'Yellow Tail',
    'Clos de los siete',
)

tic = timeit.default_timer()

ProdutoClass.cria_produto(produtos)

toc = timeit.default_timer()

print('tempo', toc - tic)