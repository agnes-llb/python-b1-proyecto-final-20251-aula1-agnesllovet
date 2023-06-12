"""
Ejercicio 1: Sistema de comida rápida
 
Fuente: Poster. Sistema Para Restaurantes de Comida Rápida, 2022
Según la Wikipedia: “El concepto de comida rápida es un estilo de alimentación donde el alimento se prepara y sirve para consumir rápidamente en establecimientos especializados”.

En este ejercicio abordaremos la implementación de un sistema simple para procesar órdenes de un negocio de comida rápida. Para ello simularemos una base de datos utilizando varios archivos en formato CSV, donde cada uno tendrá la información de los cajeros, los clientes y de los productos. El objetivo final es crear una aplicación que permita a un cajero preparar una orden para un cliente al ir agregando productos y calcular el monto total del pedido. Es importante notar que emplearemos varios paquetes que luego deben integrarse entre sí. 

Adicionalmente, los cajeros, clientes y productos deben ser convertidos en objetos, de esta manera se pondrá en práctica las técnicas del paradigma de la programación orientada a objetos. 

Finalmente, el ejercicio tiene una serie de pistas para que el estudiante pueda desarrollar y generar una solución con todo lo visto durante el desarrollo del curso.  
Descripción de las actividades
Implementar un paquete llamado 'products' que tiene dos módulos: 'container.py' y 'product.py', con la siguiente estructura:

products/
        __init__.py
        container.py
        product.py

El módulo 'container.py' contendrá una clase abstracta denominada 'Container' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases 'Wrapping', 'Bottle', 'Glass' y 'Box', es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase Wrapping se puede definir como:

class Wrapping(Container):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py' contendrá una clase abstracta denominada 'Product' con dos funciones abstractas como: 'def type(self) -> str' y 'def container(self)-> Container'.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases 'Hamburger', 'Soda', 'Drink' y 'HappyMeal', es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase 'Hamburger', se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def container(self) -> Container:
        return Wrapping()
        
Implementar un paquete llamado 'users' que tiene un módulo 'user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada 'User' que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases 'Cashier' y 'Customer', es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 
'file_manager.py' y 'converter.py', con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo 'file_manager.py' contendrá una clase 'CSVFileManager' con dos funciones:

1)	La función 'def read(self)' lee un archivo en formato CSV y exporta su resultado como un Data Frame.
2)	La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

El módulo 'converter.py' contendrá una clase denominada 'Converter' con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería 'def convert(self, dataFrame, *args) -> list'. Adicionalmente esta clase tiene un método que permite imprimir la información de los objetos 'def print(self, list)'.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases 'CashierConverter', 'CustomerConverter' y 'ProductConverter', es decir estas deben implementar el método anterior y devolver un valor. 

Por ejemplo, la clase 'CashierConverter' se puede definir como:

class CashierConverter(Converter):
  def convert(self, dataFrame):    
    cashierList = []
    for index, row in dataFrame.iterrows():      
      cashier = Cashier(str(row['dni']), row['name'], row['age'], row['timetable'], row['salary'])
      cashierList.append(cashier)
    return cashierList

La clase 'ProductConverter' se encarga de realizar la conversión de los distintos productos hacia listas. Para esto debemos pasar como un parámetro adicional la clase de cada tipo de producto, por ejemplo: 'Hamburger', 'Soda', 'Drink' y 'HappyMeal'.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada 'Order' con un constructor 'def __init__(self, cashier:Cashier, customer:Customer):', el cual que permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son 'def add(self, product: Product)', ' def calculateTotal(self) -> float' y 'def show(self)', respectivamente

Finalmente tendremos una clase principal que se llamará 'PrepareOrder' en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:
•	cashiers.csv: Información de los cajeros que harán uso del sistema.
•	customers.csv: Información de los clientes que harán uso del sistema.
•	drinks.csv: Información de los diferentes tipos de bebidas.
•	sodas.csv: Información de los diferentes tipos de gaseosas.
•	hamburgers.csv: Información de los diferentes tipos de hamburguesas.
•	happyMeal.csv: Información de los diferentes tipos de happy meals.

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 

A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Utilizar una instancia la clase 'CashierConverter' y llamar al método 'convert()' e imprimir la lista llamando al método 'print()'.
b.	Convertir clientes: Utilizar una instancia la clase 'CustomerConverter' y llamar al método 'convert()' e imprimir la lista llamando al método 'print()'.
c.	Convertir productos: Utilizar una instancia la clase 'ProductConverter' y llamar al método 'convert()' e imprimir la lista llamando al método 'print()'.
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *

    
class PrepareOrder:
 #Write your code here
 pass

