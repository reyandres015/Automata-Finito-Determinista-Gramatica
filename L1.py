# Declaracion de la clase
class AFD_ab:
    def __init__(self):

        # Definición de los estados del AFD
        self.no_terminales = {'S'}
        
        # Definición del alfabeto
        self.terminales = {'0', '1'}

        # Estado inicial
        self.estado_inicial = 'S'

        # Definición de las reglas
        self.reglas = {
            'S' : {'0':'X','1':'Y'},
            'X': {'0': 'S'},
            'Y': {'1': 'S'},
        }

        # Estados de aceptación
        self.estado_aceptado = {'S'}

    # Declaración de la funcion encargada de verificar si la cadena cumple con alguna de las reglas
    def verificar(self, cadena):
      # Definicion del estado actual
      estado_actual=self.estado_inicial
      listCadena = list(cadena) #Recorrido de la cadena de caracteres como lista.
      for i in range(len(listCadena)):
        if estado_actual is None:
          return False # Si no hay una transición definida para el símbolo, la cadena no es válida.
        elif listCadena[i] not in self.terminales:
          print("Simbolo no valido")
          return False # Si un símbolo no pertenece al alfabeto, la cadena no es válida.
        
        estado_actual=self.reglas[estado_actual].get(listCadena[i])
        estado_actual=self.reglas[estado_actual].get(listCadena[(len(listCadena) - 1) - i])
      
      return estado_actual in self.estado_aceptado
    
# Llamada de la clase
busqueda = AFD_ab()

# Ingreso de la cadena
cadena=str(input("Ingrese la cadena: "))
# Llamado de la funcion
resultado = busqueda.verificar(cadena)
print(f"La cadena '{cadena}'{' es aceptada' if resultado else ' no es aceptada'}")