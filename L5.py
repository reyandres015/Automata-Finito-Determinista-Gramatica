class L5:
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

        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False

            estado_actual = self.transiciones[estado_actual].get(simbolo, None)

            if estado_actual is None:
                return False

        return estado_actual in self.estados_aceptacion and cadena.startswith('a') and cadena.endswith('b') and ('ab' in cadena[1:-1] or cadena == 'ab')


if __name__ == "__main__":
    # Ejemplo de uso
    l5 = L5()
    cadena = ''

    # Ingreso de la cadena
    print('L5')

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

    resultado = l5.validar_cadena(cadena)  # True
    print(
        f"La cadena '{cadena}'{' es aceptada' if resultado else ' no es aceptada'}")
