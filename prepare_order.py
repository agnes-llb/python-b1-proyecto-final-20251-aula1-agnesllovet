"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
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
from datetime import datetime
from users import *
from util.converter import cashiers_read_list, customers_read_list, products_read_list, print_list 
from orders.order import Order
from products.product import Product

class PrepareOrder:
   #Write your code her
   def __init__(self, cashiers: list, customers: list, products: list, 
                input_customer: bool, input_cashier: bool, input_product: bool ):
      self.list_customers = customers
      self.list_cashiers = cashiers
      self.list_products = products
      self.input_customer = input_customer
      self.input_cashier = input_cashier
      self.input_products = input_product

   def find_cashier_dni (self, dni:str) -> Cashier:
       for cashier in self.list_cashiers:
          if cashier.dni == dni:
             return cashier
       return (f"Error. The input ID {dni} is not find in our cashiers.csv database.")

   def find_customer_dni (self, dni:str) -> Customer:
       for customer in self.list_customers:
          if customer.dni == dni:
             return customer
       return(f"Error. The input ID {dni} is not find in our customers.csv database.")   
   
   def find_product_ID (self, id:str) -> Product:
       for product in self.list_products:
          if product.id.lower() == id.lower():
             return product
       return (f"The input {id} is not find in our product database.")
   
   def get_current_datetime() -> datetime:
       now = datetime.now()
       return (now.strftime("%Y-%m-%d %H:%M:%S"))
   

# Cridem les funcions que ens llegiran els fitxers csv.
# Carregara la informació al objecte PrepareOrder 
list_cashiers=cashiers_read_list ()
#print_list (list_cashiers) 
list_customers=customers_read_list ()
#print_list (list_customers) 
list_products=products_read_list ()
#print_list (list_products)

# Creem una instancia
# Preparem una ordre
info_list_order=PrepareOrder (list_cashiers, list_customers, list_products, False, False, False)

preparing_order = True
while (preparing_order and not info_list_order.input_cashier):
    print ('-------------')
    print ('LIST CASHIERS')
    print ('-------------')
    print_list(list_cashiers)
    dni_cashier = (input ("Enter ID cashier :")) 
    cashier_ordering=info_list_order.find_cashier_dni (dni_cashier)
    if (isinstance(cashier_ordering, Cashier)):
        print ("Input Cashier for this ordering :", end = " ")
        print (cashier_ordering.describe())
        info_list_order.input_cashier=True
    else:
        print (cashier_ordering)
        print ("Do you want to continue with the order ?")
        answer=input ("Yes to continue or other key to abort ordering :")
        if answer.lower() == "yes" or answer.lower() == "y":
           preparing_order=True
        else:
           preparing_order=False

while (preparing_order and info_list_order.input_cashier and not info_list_order.input_customer):
    print ('--------------')
    print ('LIST CUSTOMERS')
    print ('--------------')      
    print_list(list_customers)
    dni_customer = (input ("Enter ID customer :"))
    customer_ordering=info_list_order.find_customer_dni (dni_customer)
    if (isinstance(customer_ordering, Customer)):
       print ("Input Customer for this ordering :", end =" ")
       print (customer_ordering.describe())
       info_list_order.input_customer=True
    else:
       print (customer_ordering)
       print ("Do you want to continue with the order ?")
       answer=input ("Yes to continue or other key to abort ordering :")
       if answer.lower() == "yes" or answer.lower() == "y":
           preparing_order=True
       else:
           preparing_order=False           

# Inicialitzem l'ordre - amb el caixer / customer entrats anteriorment
if preparing_order and info_list_order.input_cashier and info_list_order.input_customer:
    current_order = Order(cashier_ordering, customer_ordering)
    # Llistem productes
    print ('--------------')
    print ('START ORDERING')
    print ('--------------')          
    print_list (list_products)

while (preparing_order and info_list_order.input_cashier and info_list_order.input_customer and not info_list_order.input_products):
    print ('------------------------------------')
    id_product = (input ("Input ID product :"))
    product_ordering=info_list_order.find_product_ID (id_product)
    if (isinstance(product_ordering, Product)):
        current_order.add(product_ordering)
        print ("Product added :", end = " ")
        print (product_ordering.describe())
    else:
       print (product_ordering)
    
    #print ("Do you want to add another product? ")
    #print ("Yes (add product)   / No (finish ordering)")
    #print ("Show (see ordering) / List (see products)")
    #another = (input ("Abort (abort ordering). Enter selection :"))
    new_action = True
    while (new_action):
        print ('------------------------------------')
        print ("Do you want to add another product? ")
        print ("Yes (add product) / No (finish ordering)")
        print ("Show (see ordering) / List (see products) / Abort (abort ordering)")   
        another = (input ("Enter selection :"))
        if another.lower() == 'yes' or another.lower() == 'y':
           preparing_order = True
           new_action = False
        elif (another.lower() == 'no' or another.lower() =='n' and current_order.products):
           info_list_order.input_products = True
           new_action = False
        elif (another.lower() == 'show' or another.lower()=='s'):
           print ("Current Order :")
           current_order.show ()
        elif (another.lower() == 'list' or another.lower() == 'l'):
           print ("Product List :")
           print_list (list_products)
        elif (another.lower() == 'abort' or another.lower() == 'a'):
           print ('Exit seleccion selected')
           print ('The order is cancelled')
           new_action = False
           preparing_order=False
        else:
           print ('Selection not valid. Try again')       
        
if (info_list_order.input_cashier and info_list_order.input_customer and info_list_order.input_products):
    print ('-----------')
    print ('FINAL ORDER')
    print ('-----------')
    current_order.show()
    




