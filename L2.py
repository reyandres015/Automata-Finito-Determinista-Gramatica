class L2:
    def __init__(self):
        # Definición de los estados del AFD
        self.estados = {'S', 'A'}

        # Definición del alfabeto
        self.alfabeto = {'a', 'b'}

        # Definición de las transiciones
        self.transiciones = {
            'S': {'a': 'A', 'b': 'A'},
            'A': {'a': 'A', 'b': 'A'}
        }

        # Estado inicial
        self.estado_inicial = 'S'

        # Estados de aceptación
        self.estados_aceptacion = {'A'}

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        contador_a = 0
        contador_b = 0

        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                # Si un símbolo no pertenece al alfabeto, la cadena no es válida.
                print("Simbolo no valido")
                return False

            # self.transiciones[estado_actual] accede al diccionario de transiciones del estado actual
            estado_actual = self.transiciones[estado_actual].get(simbolo, None)
            # obtiene el próximo estado asociado al símbolo

            if estado_actual is None:
                # Si no hay una transición definida para el símbolo, la cadena no es válida.
                return False

            if simbolo == 'a':
                contador_a += 1
            elif simbolo == 'b':
                contador_b += 1

        return estado_actual in self.estados_aceptacion and contador_b == contador_a + 1


if __name__ == "__main__":
    # Ejemplo de uso
    l2 = L2()
    cadena = ''

    # Ingreso de la cadena
    print('L2')
    
    print('1. Consola')
    print('2. Archivo de texto')
    menu = str(input('Ingrese la opción que desea:'))

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

    resultado = l2.validar_cadena(cadena)  # True
    print(
        f"La cadena '{cadena}'{' es aceptada' if resultado else ' no es aceptada'}")
