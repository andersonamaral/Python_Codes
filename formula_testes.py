'''
O código abaixo recebe um input em numeros separados por viruglas , calcula o resultado de acordo com a equação
Q = Raiz quadrada de [(2 * C * D)/H] pra cada um e retorna o resultado da mesma maneira: separado por virgulas
Ps: c  e h são fixos respectivamente 50 e 30, pois o foco era no estilo do output

'''
#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(math.sqrt(2*c*float(d)/h))))

print(','.join(value))

