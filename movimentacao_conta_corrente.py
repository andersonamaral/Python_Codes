'''
D é o deposito, e S é o saque.
Exemplo de uso:
D 500
D 400
S 300

Aperte o enter duas vezes e o resultado sera 600
'''




import sys
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="S":
        netAmount-=amount
    else:
        pass
print(netAmount)
