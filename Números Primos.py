def primos(qua):
    p = [2, 3]
    i = 1
    con = p[i]
    n = 5
    while  n<qua:                           #loop infinito
        z = n % con
        if z == 0:
            n+=2
            i=1
            con=p[i]
        elif (z != 0) and (i>=len(p)-1):
            p+=[n]
            n+=2
            i=1
            con = p[i]
        elif (z != 0) and (i<len(p)-1):     #verifica se o i esta no range de indices da lista de numeros primos
            i+=1                            #incrementa o i para analisar o proximo numero primo
            con = p[i]                      #assume o valor do proximo numero primo
    return str(p) + '\n'
arq =  open('primos.txt', 'w')
p = primos(100000)
arq.write(p)
arq.close()