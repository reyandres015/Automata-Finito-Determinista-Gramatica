# Declaración de la clase
class AFD_ab:
    def __init__(self):

        # Definición de los estados del AFD
        self.no_terminales = {'S', 'X', 'Y'}

        # Definición del alfabeto
        self.terminales = {'0', '1'}

        # Estado inicial
        self.estado_inicial = 'S'

        # Definición de las reglas
        self.reglas = {
            'S': {'0': 'X', '1': 'Y'},
            'X': {'0': 'S'},
            'Y': {'1': 'S'},
        }

        # Estados de aceptación
        self.estado_aceptado = {'S'}

    # Declaración de la funcion encargada de verificar si la cadena cumple con alguna de las reglas
    def verificar(self, cadena):
        # Definicion del estado actual
        estado_actual = self.estado_inicial
        # Recorrido de la cadena de caracteres como lista.
        listCadena = list(cadena)
        for i in range(len(listCadena)):
            if estado_actual is None:
                # Si no hay una transición definida para el símbolo, la cadena no es válida.
                return False
            elif listCadena[i] not in self.terminales:
                print("Simbolo no valido")
                # Si un símbolo no pertenece al alfabeto, la cadena no es válida.
                return False

            estado_actual = self.reglas[estado_actual].get(listCadena[i])
            estado_actual = self.reglas[estado_actual].get(
                listCadena[(len(listCadena) - 1) - i])

        return estado_actual in self.estado_aceptado


# Llamada de la clase
busqueda = AFD_ab()

cadena = ''

# Ingreso de la cadena
print('L1 - NUMEROS CAPICÚOS')
print('1. Consola')
print('2. Archivo de texto')
menu = str(input('Ingrese la opción que desea: '))

if menu == '1':
    cadena = str(input("Ingrese la cadena: "))
elif menu == '2':
    nombreArchivo = str(input('Ingrese el nombre del archivo: '))
    with open(nombreArchivo, 'r') as file:
        cadena = file.read()
        print(cadena)
else:
    print('Ingrese un opción valida')
    print('Fin del programa')

# Llamado de la función
resultado = busqueda.verificar(cadena)
if resultado:
    print('Si es un numero capicúo:',  cadena, '|', cadena[::-1])
else:
    # [::-1] => invertir numero para imprimirlo
    print('No es un numero capicúo:',  cadena, '|', cadena[::-1])
