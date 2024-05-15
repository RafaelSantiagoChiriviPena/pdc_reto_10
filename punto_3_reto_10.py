if __name__ == "__main__":
    try: 
        lista = []  # declaracion de lista vacia

        len_arreglo : int = int(input("Defina el numero de componentes que tendra el arreglo: "))    # ingreso de numero de componentes
        while len_arreglo < 1:  # limite solo para componentes positivos    
            len_arreglo = int(input("El valor ingresado no es valido, intentelo de nuevo: "))

        while len(lista) <= (len_arreglo - 1): # condicion para detener el ingreso de datos una vez el numero de estos sea igual al numero de componentes ingresado anteriormente
            dato : float = float(input("Ingrese el dato para el arreglo: ")) # ingreso del dato numerico real
            lista.append(dato)  # se agrega el dato a la lista anteriormente establecida

        print(f"La lista resultante es \n {lista}")     # impresion de la lista resultante

        ceros : int = lista.count(0)    # asignacion del numero de ceros en la lista a una variable
        for i in range (0, ceros): # recorrido en un rango desde 0 hasta el numero de ceros en la lista
            lista.remove(0)     # se elimina por defecto el primer cero encontrado de izquierda a derecha
            lista.append(0.0)   # se agrega al final de la lista
        print(f"La lista resultante, al reacomodar todos los 0 al final de la lista es \n {lista}")     # impresion de la lista resultante
        
    except ValueError:
        print("El valor ingresado no se trata de un numero entero")