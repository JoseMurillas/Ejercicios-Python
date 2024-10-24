def conjuntos (numero):
    if(numero % 2 != 0):
        return('Numero impar')
    else:
        return('numero par')
    
numero = int(input("Ingresa el numero entero \n"))
resultado = conjuntos(numero)
print(f'{resultado}')
