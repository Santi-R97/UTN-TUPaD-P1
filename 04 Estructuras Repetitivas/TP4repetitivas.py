# Nombre: Santiago Gabriel Rodriguez
#
#                   TP 4 Estructuras Repetitivas
#                    
# Actividades:

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101): # pongo el 101 para que incluya hasta el 100
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input('Ingrese un numero entero: '))
digitos = len(str(num)) # pasamos el numero a string y usamos la funcion len() para que nos devuelva la cantidad de caracteres de un string
print(f'La cantidad de digitos de {num} es: {digitos}')

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese otro numero entero: '))
acumulador = 0

for i in range(num1+1,num2): # ponemos el +1 para que exluya sumar el num1 ingresado
    acumulador = acumulador + i # en el acumulador  vamos sumando cada numero que se va iterando

print(f'La suma de los numeros comprendidos excluyendo los dos valores ingresados es: {acumulador}')

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print('Ingrese un numero entero, para detener el programa ingrese un 0')
num = int(input()) # hago una primera variable num para que el while haga un primer bucle
suma = 0
while num != 0: # pongo que sea distinto de cero para poder terminar el programa
    suma = suma + num # mientras ingrese un numero entero se va a ir sumando o restando en el acumulador hasta que terminen el programa
    num = int(input('Ingrese otro numero: ')) # con el 2do num mientras sea distinto de 0 se va a volver a repetir el bucle

print(f'La suma de los numeros ingresados es {suma}')

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random # importamos la liberia random para poder usar una funcion de azar

num  =  int(input('Adivina el numero secreto entre 0 y 9, Ingrese su numero: '))
aleatorio = random.randint(0, 9) # con esta funcion hacemos que se cree un numero aleatorio del 0 al 9
intentos = 1 # le damos valor de 1 por si el usuario adivina en el primer intento, ya que no entra en el bucle.

while num != aleatorio: # mientras la variable num que es el numero que ingresa el usuario sea distinto de aleatorio se repite el ciclo
    num  =  int(input('Fallaste, intenta con otro numero: '))
    intentos += 1 # en la variable intenos vamos guardando las veces que el usuario no adivino el numero creado por la funcion de azar

print(f'Ganaste, adivinaste en el intento numero {intentos}.')

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,0,-2): # para hacer el decremento pongo 100 primero para que empiece a iterar desde ese numero
    print(i)              # y pongo -2 para que vaya restando de a 2 y muestre solo los numeros pares

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num_positivo = int(input('Ingrese un numero entero POSITIVO: '))
suma = 0

if num_positivo > 0: # usamos esta instruccion para que el programa se asegure de que se use un numero positivo
    for i in range(num_positivo + 1): # ponemos el +1 para asegurarnos de que llegue al numero ingresado
        suma += i # con esta instruccion hacemos que cada iteracion se sume y se guarde en la variable suma
    print(f'La suma de los numeros comprendidos entre 0 y {num_positivo} es: {suma}')
else:
    print('El numero ingresado no es positivo')

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad = 100 # creamos una variable cantidad para solo modificar su valor y evitar su cambio en diferentes lugares
pares =  0
impares =  0 # creamos estas variables para guardar tras cada iteracion su numero correspondiente
positivos =  0
negativos =  0

for i in range(cantidad): # usamos la variable cantidad para darle un numero de veces que queremos que se repita el ciclo
    num = int(input('Ingrese un numero entero: '))
    if num == 0: # como 0 no es par, ni impar, ni negativo, ni positivo, usamos un if para evitar meterlo en alguna variable creada
        pass # usamos el pass para que la condicion no haga nada y no afecte el programa
    else:
        if num > 0: # usamos un if para saber si es positivo y con el else si es el caso contrario
            positivos += 1 # con esta instruccion guardamos cada numero positivo en la variable de positivos
        else:
            negativos += 1

        if num % 2 == 0: # usamos otro if para repetir el proceso de arriba y el else para el caso contrario
            pares += 1
        else:
            impares += 1

print(f'Hay {pares} numeros pares, {impares} numeros impares, {positivos} numeros positivos, {negativos} numeros negativos.')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad = 100 # creamos una variable cantidad para solo modificar su valor y evitar su cambio en diferentes lugares
suma = 0
for i in range(cantidad): # usamos la variable cantidad para darle un numero de veces que queremos que se repita el ciclo
    num = int(input('Ingrese un numero entero: '))
    suma += num # usamos esta instruccion para sumar cada numero que el usario ingrese en cada iteracion y los guarde en la variable suma

print(f'El promedio de los numeros ingresados es de {suma/cantidad}') # en el print ponemos la operacion necesaria para sacar el promedio 
#                                                                     # usando las variables que ya tenemos definidas y dar el resultado final

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input('Ingrese un numero: '))
if num > 0: # usamos un if por si el usuario quisiera invertir un numero negativo
    invertido = int(str(num)[::-1]) # pasamos el numero a string y usamos la instruccion [::-1] para invertir el numero
else:                               # y usamos el int para volverlo a convertir en un numero entero
    invertido = int("-" + str(abs(num))[::-1]) # para invertir un numero negativo es igual pero hay que sumarle el '-' al str
print(invertido)                               # y usar la funcion abs













