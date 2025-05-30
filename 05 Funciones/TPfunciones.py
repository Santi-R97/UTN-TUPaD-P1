# Nombre: Santiago Gabriel Rodriguez
#
#                   Practico 2: Funciones
#                    
# Actividades:

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

saludar_usuario(input('Ingrese su nombre: '))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

informacion_personal(input('Ingrese su nombre: '), input('Ingrese su apellido: '), input('Ingrese su edad: '), input('Ingrese su lugar de residencia: '))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio
# al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.1415 * radio ** 2
    print(f'El area del circulo es : {area}')

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1415 * radio
    print(f'El perimetro del circulo es : {perimetro}')

radio = float(input('Ingrese el radio del circulo: '))
calcular_area_circulo(radio), calcular_perimetro_circulo(radio)

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado
# usando esta función.

def segundos_a_horas(segundos):
    hora = segundos / 3600
    print(f'La cantidad de horas correspondientes a los segundos ingresados es: {hora}')

segundos_a_horas(int(input('Ingrese una cantidad en segundos: ')))

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    resultado = 0
    for i in range(1, 11):
        resultado = numero  * i
        print(f'{numero} x {i} = {resultado}')

tabla_multiplicar(int(input('Ingrese un numero: ')))

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    resultadosuma = (a + b)
    resultadoresta = (a - b)
    resultadomulti = (a * b)
    resultadodivi = (a / b)
    print(f'Sumar ambos numeros es ({resultadosuma}), restarlos ({resultadoresta}), multiplicarlos ({resultadomulti}), dividirlos ({resultadodivi})')

operaciones_basicas(int(input('Ingrese un numero: ')), int(input('Ingrese otro numero: ')))

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva
# el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f'Su indice de masa corporal es: {round(imc, 2)}')

calcular_imc(float(input('Ingrese su peso en Kg: ')),float(input('Ingrese su altura en Metros: ')))

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}° Celsius equivale a {fahrenheit}° Fahrenheit')

celsius_a_fahrenheit(float(input('Ingrese una temperatura en grados Celsius: ')))

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar
# los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f'El promedio de los numeros ingresados es: {promedio}')

calcular_promedio(int(input('Ingrese un numero: ')),int(input('Ingrese un segundo numero: ')),int(input('Ingrese un tercer numero: ')))