#se codigo acha todos os numeros dividos por 7 mas que nao multiplos de 5 e nem de 5,no intervalo de 3000 a 10000 e os imprime em sequencia

l=[]
for i in range(3000, 10000):
    if (i%7==0) and (i%5!=0) and (i%4!=0):
        l.append(str(i))
print(','.join(l))
                                                                                                                                                                                                                                   
