'''

Aluno: Lucas Airam Castro de Souza
Resumo: Programa para calcular a raiz com a precisão n de casas decimais


def raiz(numero, casas_decimais=0):
    if ((numero == 0) or (numero == 1)):
        return "O resultado eh: " + str(numero)
    elif (numero<0):
        return "A raiz nao existe no conjunto real"
    else:       
        resultado = [0]
        if (casas_decimais == 0):
            while True:
                if ((resultado[0]+1)**2<numero):
                    resultado[0]+=1
                else:
                    return resultado[0]
        else:
            for cont in range(casas_decimais):
                resultado+=[0]
            primeiro_numero=0
            while True:
                if ((primeiro_numero+1)**2<numero):
                    primeiro_numero+=1
                else:
                    resultado[0]=str(primeiro_numero)
                    casas_corretas = 1
                    while (casas_corretas < len(resultado)):    
                        cont1=0
                        while ((cont1 < 10) and (cont1 < len(resultado))):
                            numero_parcial = ""
                            print resultado
                            for cont2 in range(casas_corretas):
                                numero_parcial+=str(resultado[cont2])
                                print resultado
                                print resultado [1]
                                print resultado[cont2]
                            if ((int(numero_parcial)+1)**2<numero):
                                cont3 = int(resultado[casas_corretas])+1
                                resultado[casas_corretas]=str(cont3)
                            else:
                                resultado[casas_corretas]=str(cont1)
                                casas_corretas+=1
                            cont1+=1
                    resultado_final = ""
                    for cont4 in range(casas_corretas):
                        resultado_final+=resultado[cont4]      
                    return int(resultado_final)
        
        
'''
def raiz(numero):
    casas_decimais=18
    if ((numero == 0) or (numero == 1)):
        return "O resultado eh: " + str(numero)
    elif (numero<0):
        return "A raiz nao existe no conjunto real"
    else:
        posicao = 0
        casa_decimal = 10**posicao
        resultado_parcial = 0.0
        while (-posicao != casas_decimais+1):
          #  print 'resultado: ' +str(resultado_parcial)
          #  print 'casa decimal: ' +str(casa_decimal)
          #  print 'posicao: ' +str(posicao)
            if ((resultado_parcial+casa_decimal+(casa_decimal*1))**2 < numero):
                casa_decimal+=(10**posicao)*1
                resultado_parcial+=casa_decimal
            else:
                posicao-=1
                casa_decimal=10**posicao
        return resultado_parcial
                
