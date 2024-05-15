def prom (lista : list, longitud : int) -> float:   # definir la funcion para el promedio de lista
    sumatoria : float = 0.0     # establecer la constante para la sumatoria de los datos de la funcion en 0

    for i in range (0 , len(lista)):    # bucle para recorrer la lista y todo sus elementos
        sumatoria += float(lista[i])    # sumar a la constante de sumatoria el valor de los componentes

    return sumatoria / longitud     # retornar el promedio de los datos (sumatoria de datos / numero de datos)

if __name__ == "__main__":
    try:
        lista = []  # establecer la lista como vacia

        len_arreglo : int = int(input("Defina el numero de componentes que tendra el arreglo: "))   # ingreso de numero de componentes
        while len_arreglo < 1:  # limite para solo componentes positivos
            len_arreglo = int(input("El valor ingresado no es valido, intentelo de nuevo: "))

        while len(lista) <= (len_arreglo - 1): # condicion para detener el ingreso de datos una vez el numero de estos sea igual al numero de componentes ingresado anteriormente
            dato : float = float(input("Ingrese el dato para el arreglo: ")) # ingreso del dato numerico real
            lista.append(dato)  # se agrega el dato a la lista anteriormente establecida

        print(f"La lista resultante es \n {lista}")     # impresion de la lista
        
        promedio = prom(lista, len_arreglo)     # asignar el valor de la funcion aplicada a la lista a una variable
        print(f"El promedio de la lista es {promedio}")     # impresion del resultado   

    except ValueError:
        print("El valor ingresado no se trata de un numero entero")