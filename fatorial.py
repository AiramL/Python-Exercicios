'''

Aluno: Lucas Airam Castro de Souza
Programa para calcular fatorial de um numero n

'''

def fatorial(numero):
    if (numero == 0) or (numero == 1):
        return numero
    elif (((type(numero)!=long) or (type(numero)!=int)) and (numero<0)):
        return "Operacao definida apenas para o conjunto dos numeros inteiros positivos"
    resultado = numero
    for contador in range(1,numero):
        resultado *= contador
    return resultado

fatorial(10)
