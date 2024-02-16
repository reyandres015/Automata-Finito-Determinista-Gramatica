class L4:
    def __init__(self):
        # Definición del autómata
        self.estados = {'S', 'A'}
        self.alfabeto = {'a', 'b'}
        self.estado_inicial = 'S'
        self.estado_aceptacion = {'A'}
        self.transiciones = {
            'S': {'a': 'A', 'b': 'A'},
            'A': {'a': 'A', 'b': 'A'}
        }

    def validar_cadena(self, cadena):
        # Inicialización del autómata
        estado_actual = self.estado_inicial
        count_a = 0
        count_b = 0

        # Procesamiento de la cadena
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return "Cadena no válida. Contiene símbolos no permitidos."

            estado_actual = self.transiciones[estado_actual].get(simbolo, None)

            if estado_actual is None:
                return False  # Cuando se indican simbolos en la cadena de texto que NO hacen parte del alfabeto

            # Conteo de 'a' y 'b'
            if simbolo == 'a':
                count_a += 1
            elif simbolo == 'b':
                count_b += 1

        # Verificación del estado final y de la condición {abb|ab}
        if estado_actual == 'A' and count_a == 1 and (count_b == 1 or count_b == count_a + 1):
            return True
        else:
            return False


if __name__ == "__main__":

    l4 = L4()
    cadena = ''

    # Ingreso de la cadena
    print('L4')
    
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

    resultado = l4.validar_cadena(cadena)  # True
    print(
        f"La cadena '{cadena}'{' es aceptada' if resultado else ' no es aceptada'}")
