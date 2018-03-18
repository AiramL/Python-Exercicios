def div(nu):
    p = [2, 3]
    i = 1
    con = p[i]
    n = 5
    while  con<n:                           #loop infinito ate que chegue no break
        #Esse bloco cria uma matriz com numeros primos
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
        elif (z != 0) and (i<len(p)-1):
            i+=1
            con = p[i]
        # Fim do bloco que cria a matriz com numeros primos
        ###################################################
        # Bloco que fatora nu em numeros primos
        d = []  
        if nu <= p[len(p) - 1]:                                 # Compara o numero com o maior elemento dos numeros primos
            cont = 0                                            # Variavel de controle
            quo_divisao = float(nu)                             # Variavel de controle
            while ((quo_divisao != 1) and (cont < len(p) - 1)): # Condicao para que o numero esteja fatorado
                if quo_divisao % p[cont] == 0:
                    d += [p[cont]]
                    quo_divisao /= p[cont]
                else:
                    cont += 1
        # Fim do bloco que cria uma matriz com os fatores de nu
        ##################################################
        #Inicio do bloco que conta o numero de divisores de um numero
        ex = []                         #Eh criada uma matriz nula primeiramente
        for v in range(len(d)):         #Preeche a matriz nula com a quantidade de elementos existentes na matriz d
            ex+=[0]
        a = 0
        for q in range(len(d)):
            ex[a] = d.count(d[q])
            if q+1 < len(d):
                if d[q] != d[q+1]:
                    a+=1
                else:
                    pass
        while 0 in ex:                  # Remove zeros da matriz
            ex.remove(0)
        for z in range(len(ex)):        # Adiciona 1 a cada elemento da matriz
            ex[z]+=1
        resultado = ex[0]
        for g  in range(1,len(ex)):
            resultado*=ex[g]

        #print ex
        print nu
        print d
        print p
        print resultado
        if resultado == 16:
            #print '\n\n\n'+str(resultado)
            #print '\n\n\n\n ' + str(n)
            #print '\n\n\n\n o primeiro numero eh: ' + str(nu)
            #print '\n\n\n\n o modulo da divisao eh: ' + str(nu%500500507)
            break
        else:
            nu+=1



    #print nu
    #print d
    #print di
   # print con
    #print ex

nu = 2
print div(nu)
#x = div(nu)
#print x%500500507
#print 500500507%x
#print x