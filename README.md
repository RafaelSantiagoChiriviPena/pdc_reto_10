# pdc_reto_10
### Soy Rafael Santiago Chirivi Peña y pertenezco al grupo de "Fenomenoides", adelante se muestra nuestro logo 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### A continuacion, se muestran las soluciones propuestas a los distintos puntos de este reto

## 1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
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
```

## 2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```python
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
```

## 3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```python
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
```

## 4. Revisar que son los algoritmos de sorting, entender bubble-sort
