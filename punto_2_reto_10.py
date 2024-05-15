prod_punto : int = 0    # declaracion de la constante para el producto punto como entero 0 

if __name__ == "__main__":
    try:
        lista_A = []    #  declaracion de lista vacia A
        lista_B = []    #  declaracion de lista vacia B
        
        len_arreglo : int = int(input("Defina el numero de componentes que tendran los arreglos: "))    # ingreso de numero de componentes
        while len_arreglo < 1:  # limite solo para componentes positivos
            len_arreglo = int(input("El valor ingresado no es valido, intentelo de nuevo: "))

        while len(lista_A) <= (len_arreglo - 1):    # condicion para detener el ingreso de datos una vez el numero de estos sea igual al numero de componentes ingresado anteriormente
            dato : float = float(input("Ingrese el dato numerico entero para el arreglo A: "))  # ingreso del dato numerico entero
            while dato % 1 != 0:    # limite para ingreso de solo numeros enteros
                dato = float(input("El numero ingresado no es valido, por favor solo ingrese numeros enteros: "))
            lista_A.append(dato)    # se agrega el dato a la lista anteriormente establecida

        print(f"La lista resultante es \n {lista_A}")   # impresion de la lista

        while len(lista_B) <= (len_arreglo - 1):    # condicion para detener el ingreso de datos una vez el numero de estos sea igual al numero de componentes ingresado anteriormente
            dato : float = float(input("Ingrese el dato numerico entero para el arreglo B: "))   # ingreso del dato numerico entero
            while dato % 1 != 0:    # limite para ingreso de solo numeros enteros
                dato = float(input("El numero ingresado no es valido, por favor solo ingrese numeros enteros: "))
            lista_B.append(dato)    # se agrega el dato a la lista anteriormente establecida

        print(f"La lista resultante es \n {lista_B}")   # impresion de la lista

        for i in range(0, len(lista_A)):    # recorrido para los datos de los arreglos
            sumatoria = int(lista_A[i]) * int(lista_B[i])   # asignacion del producto de cada componente de los arreglos (x_1 * y_1... x_n * y_n) para n como el numero de componentes establecido
            prod_punto += sumatoria     # adicion del producto al valor del producto punto, siendo la sumatoria de los productos de los componentes de los vectores
        print(f"El producto punto entre los vectores A = {lista_A} y B = {lista_B} es igual a A . B = {prod_punto}")    # impresion del producto punto entre las listas
        
    except ValueError:
        print("El valor ingresado no se trata de un numero")