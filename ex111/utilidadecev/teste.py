import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex111.utilidadecev import moeda,dado

p = float(input('Digite o preço: R$ '))
moeda.resumo(p,20,12)