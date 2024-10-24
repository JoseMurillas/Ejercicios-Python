def operaciones (operacion, a , b): 
    return {
    '1': lambda a,b: a + b,
    '2': lambda a,b: a - b,
    '3': lambda a,b: a * b, 
    '4': lambda a,b: a / b if b != 0 else "División no definida" 
}

operacion = input('Ingresa la operación aritmetica \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n')
numero1 = float(input('Ingrese el numero 1\n'))
numero2 = float(input('Ingrese el numero 2\n'))
resultado = operaciones(operacion, numero1, numero2)[operacion](numero1, numero2) 
print(f'El resultado es: {resultado}')