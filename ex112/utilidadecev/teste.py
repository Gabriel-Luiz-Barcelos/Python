import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex112.utilidadecev import moeda
from ex112.utilidadecev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p,20,12)