# n = input ("Por favor, ingrese su nombre: ")

# radio = 5
# print("El volumen de la esfera es: ", 4/3 * 3.1416 * radio**3)

# print(abs(round(-34.2765, 1)))

# print(str(float(str(2) * 3 + "1.123")) + "321")

#Actividad 2
def cambiar_valores(x1, x2, x3):
    x1, x2, x3 = x3, x1, x2
    return x1, x2, x3

def cambiar_valores_2(x1, x2, x3):
    aux=x1
    x1=x2
    x2=x3
    x3=aux
    return x1, x2, x3

# Actividad 3
def calcular_IVA(precio):
    IVA = precio * 0.19
    propina = precio * 0.10
    total = precio + IVA + propina
    rta = "Para la compra realizada, el valor que corresponde al IVA es de $" + str(IVA) + " pesos y la propina es de $"+ str(propina) + " pesos, para un gran total de $"+ str(total) + " pesos"
    return rta
# print(calcular_IVA(10000))

#Actividad 4
def perfil_estudiante():
    print("Por favor, ingrese los datos de los estudiantes")
    nombre_1 = input("Por favor, ingrese su nombre: ")
    edad_1 = input("Por favor, ingrese su edad: ")
    nombre_2 = input("Por favor, ingrese su nombre: ")
    edad_2 = input("Por favor, ingrese su edad: ")
    nombre_3 = input("Por favor, ingrese su nombre: ")
    edad_3 = input("Por favor, ingrese su edad: ")
    rta = nombre_1 + " este año cumple " + edad_1 + " años. "
    rta += "\n" + nombre_2 + " este año cumple " + edad_2 + " años. "
    rta += "\n" + nombre_3 + " este año cumple " + edad_3 + " años. "
    rta += "\n" + "El promedio de edad entre los estudiantes es de " + str((int(edad_1) + int(edad_2) + int(edad_3)) / 3) + " años."
    rta += "\n" + "La diferencia de edad entre el mayor y el menor estudiante " + str(max(int(edad_1), int(edad_2), int(edad_3)) - min(int(edad_1), int(edad_2), int(edad_3))) + " años."
    return rta

# print(perfil_estudiante())
print("El programa ha comenzado.")
nombre_1 = input("Por favor, ingrese su nombre: ")


def ordenar_enteros(a: int, b: int, c: int)->str:
    """ Ordenar 3 enteros
    Parámetros:
      a (int): El primero de los enteros a ordenar
      b (int): El segundo de los enteros a ordenar
      c (int): El tercero de los enteros a ordenar
    Retorno:
      str: Cadena de caracteres con los enteros ordenados de  mayor a menor, separados por coma
    """
    minimo = min(a, b, c)
    maximo = max(a, b, c)
    medio = (a + b + c) - minimo - maximo
    return str(maximo) + ", " + str(medio) + ", " + str(minimo)

def calcular_total_pan_comprado(frescos: int, viejos: int)->int:
    """ Pan del día anterior
    Parámetros:
      frescos (int): Cantidad de panes frescos comprados
      viejos (int): Cantidad de panes del día anterior comprados
    Retorno:
      int: Valor total a pagar por el pan comprado
    """
    rta = frescos * 450 + (viejos * 450 * 0.4)
    return rta 