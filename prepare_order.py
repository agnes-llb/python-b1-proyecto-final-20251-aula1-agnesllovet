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
# Imports from other moduls
from datetime import datetime
from users import Cashier, Customer
from util.converter import cashiers_read_list, customers_read_list, products_read_list, print_list, save_order_information_csv
from orders.order import Order
from products.product import Product

"""
    Class : PrepareOrder manages the process of preparing a sales order.
    It allows searching cashiers, customers and products by ID/DNI
    and provides utility methods related to the order process.
"""
class PrepareOrder:
   """
   Initializes the PrepareOrder object.
   Args:
      cashiers (list): List of Cashier objects.
      customers (list): List of Customer objects.
      products (list): List of Product objects.
      preparing_order (bool): Indicates if an order is being prepared.
      input_customer (bool): Customer input state.
      input_cashier (bool): Cashier input state.
      input_products (bool): Products input state.
    """
   def __init__(self, cashiers: list, customers: list, products: list, preparing_order: bool,
                input_customer: bool, input_cashier: bool, input_products: bool ):
      self.list_customers = customers
      self.list_cashiers = cashiers
      self.list_products = products
      self.preparing_order = preparing_order
      self.input_customer = input_customer
      self.input_cashier = input_cashier
      self.input_products = input_products

   """
   Searches for a cashier by DNI.
   Args:
        dni (str): DNI of the cashier.
   Returns:
        cashier / None: cashier object if found, if not None
   """
   def find_cashier_dni (self, dni:str) -> Cashier:
       # Iterate in the self list cashiers
       for cashier in self.list_cashiers:
          # for every cashier compare with the input dni
          if cashier.dni == dni:
             # if find return the cashier
             return cashier
       # If not find return None   
       return None 
   
   """
   Searches for a customer by DNI.
   Args:
        dni (str): DNI of the customer.
   Returns:
        customer / None: customer object if found, if not None
   """  
   def find_customer_dni (self, dni:str) -> Customer:
       # Iterate in the self list customers
       for customer in self.list_customers:
          # for every customer compare withthe input dni
          if customer.dni == dni:
             # If find return customer
             return customer
       # not find return None   
       return None

   """
   Searches for a product by ID.
   Args:
        id (str): ID of the product.
   Returns:
        product / None: product object if found, if not None
   """  
   def find_product_ID (self, id:str) -> Product:
       # Iterate in the list of products
       for product in self.list_products:
          # compare all products ID lowercase with the input id lowercase
          if product.id.lower() == id.lower():
             # If find return product
             return product
       # If not find return none   
       return None 

   """
   Returns the current datetime.
   Returns:
        datetime: Current system date and time.
   """
   def get_current_datetime(self) -> datetime:
       # return current datatime
       return (datetime.now())

""" 
select_cashier : Allows the user to select a cashier for the current order.
This function displays the list of available cashiers and asks the user
to enter a cashier DNI. The selection process continues until a valid
cashier is selected or the order is aborted by the user.

The function updates the state of the PrepareOrder object:
    - input_cashier is set to True when a cashier is successfully selected
    - preparing_order is set to False if the user aborts the process

Args:
    info_list_order (PrepareOrder): Object that contains the lists of
            cashiers and the current order state.

Returns:
    Cashier | None: The selected Cashier object if successful,
    None if the order is aborted.
"""
def select_cashier (info_list_order: PrepareOrder) -> Cashier| None:
    # init cashier_ordering to None in the case the while is not executing 
    cashier_ordering = None
    # execute while till oredring is aborting or cashier selected successful
    while (info_list_order.preparing_order and not info_list_order.input_cashier):
        # Shows the cashier list 
        print ('-------------')
        print ('LIST CASHIERS')
        print ('-------------')
        print_list(info_list_order.list_cashiers)
        # Ask for the cashier DNI
        dni_cashier = (input ("Enter DNI cashier :")) 
        # Find the input dni in the list of cashiers
        cashier_ordering=info_list_order.find_cashier_dni (dni_cashier)
        # If the cashier is found succesfully
        if (cashier_ordering is not None):
            print ("Input Cashier for this ordering :", end = " ")
            print (cashier_ordering.describe())
            info_list_order.input_cashier=True
        # If the cashier is not found or the input is not correct
        else:
            print (f"Error. The input DNI {dni_cashier} is not found in our customers.csv database.")
            # Ask to the user if want continue or abort
            print ("Do you want to continue with the order ?")
            answer=input ("Yes to continue or other key to abort ordering :")
            # Consider the word "yes" or "y" as afirmative answer 
            if answer.lower() == "yes" or answer.lower() == "y":
               info_list_order.preparing_order=True
            # in case that the porcess aborts set the preapring order to False
            else:
               info_list_order.preparing_order=False
    # return cashier or none
    return cashier_ordering
     

""" 
select_customer : Allows the user to select a customer for the current order.
This function displays the list of available customers and asks the user
to enter a customer DNI. The selection process continues until a valid
customer is selected or the order is aborted by the user.

The function updates the state of the PrepareOrder object:
    - input_customer is set to True when a customer is successfully selected
    - preparing_order is set to False if the user aborts the process

Args:
    info_list_order (PrepareOrder): Object that contains the lists of
            cashiers and the current order state.

Returns:
    Customer | None: The selected Customer object if successful,
    None if the order is aborted.
"""
def select_customer (info_list_order: PrepareOrder) -> Customer | None:
    # init cashier_ordering to None in the case the while is not executing 
    customer_ordering = None
    # execute till ordering is aborting or cashier selected successful
    while (info_list_order.preparing_order and info_list_order.input_cashier and not info_list_order.input_customer):
        # Shows the customer list 
        print ('--------------')
        print ('LIST CUSTOMERS')
        print ('--------------')      
        print_list(info_list_order.list_customers)
        # Ask for the cashier DNI
        dni_customer = (input ("Enter DNI customer :"))
        # Find the input dni in the list of customers
        customer_ordering=info_list_order.find_customer_dni (dni_customer)
        # If the customer is found succesfully
        if (customer_ordering is not None):
           print ("Input Customer for this ordering :", end =" ")
           print (customer_ordering.describe())
           info_list_order.input_customer=True
        # If the customer is not found or the input is not correct
        else:
           print (f"Error. The input DNI {dni_customer} is not find in our customers.csv database.")
           print ("Do you want to continue with the order ?")
           answer=input ("Yes to continue or other key to abort ordering :")
           # Consider the word "yes" or "y" as afirmative answer
           if answer.lower() == "yes" or answer.lower() == "y":
               info_list_order.preparing_order=True
           else:
               info_list_order.preparing_order=False           
    # return customer or none
    return customer_ordering

"""
select_products: Allows the user to add products to the current order.
    This function repeatedly asks the user to enter product IDs and adds
    the selected products to the order. 
    After each product selection, the user can choose to:
    - add another product
    - finish the order
    - show the current order
    - list all available products
    - abort the order

    The function update the state of the PrepareOrder object:
    - input_products is set to True when the user finishes selecting products
    - preparing_order is set to False if the user aborts the order
    Args:
        info_list_order (PrepareOrder): Object that contains the product list
            and the order state.
        current_order (Order): The order object where selected products will be added.
    Returns:
        None
"""
def select_products (info_list_order: PrepareOrder, current_order: Order) -> None:
    # execute till user aborts or finish order   
    while (info_list_order.preparing_order and info_list_order.input_cashier and 
             info_list_order.input_customer and not info_list_order.input_products):    
        # Ask the product ID to include in the order
        print ('------------------------------------')
        id_product = (input ("Input ID product :"))
        # Find ID product in the list of products 
        product_ordering=info_list_order.find_product_ID (id_product)
        # If the product is found include in the order
        if (product_ordering is not None):
            # Add product to the order
            current_order.add(product_ordering)
            # product description is shown 
            print ("Product added :", end = " ")
            print (product_ordering.describe())
        # If the product is not find show error
        else:
           print (f"The input {id_product} is not find in our product database.")
        # After select product ID (succesful or not) - Show options
        new_action = True
        while (new_action):
            # Show options 
            print ('------------------------------------')
            print ("Do you want to add another product? ")
            print ("Yes (add product) / No (finish ordering)")
            print ("Show (see ordering) / List (see products) / Abort (abort ordering)")   
            another = (input ("Enter selection :"))
            # Option "yes" add new product 
            if another.lower() == 'yes' or another.lower() == 'y':
               info_list_order.preparing_order = True
               new_action = False
            # Option "no" the order is finish no more products
            elif ((another.lower() == 'no' or another.lower() =='n') and current_order.products):
               info_list_order.input_products = True
               new_action = False
            # Option "show" Show the current order till now
            elif (another.lower() == 'show' or another.lower()=='s'):
               print ("Current Order :")
               current_order.show ()
            # Option "list" list all the products   
            elif (another.lower() == 'list' or another.lower() == 'l'):
               print ("Product List :")
               print_list (info_list_order.list_products)
            # option "abort" the order is cancelled
            elif (another.lower() == 'abort' or another.lower() == 'a'):
               print ('Exit seleccion selected')
               print ('The order is cancelled')
               new_action = False
               info_list_order.preparing_order=False
            # Another option - show the message again 
            else:
               print ('Selection not valid. Try again')
               if (not current_order.products):
                    print ('No selected product. Select product or Abort process')       
    return None


"""
    Main function of application.

    This function controls the full preparation order:
       Loads data from CSV files (cashiers, customers, products).
       Initializes the order preparation process.
       Allows the user to select a cashier, a customer 
       Create a order and add all the products.
       Creates and displays the final order.
       Saves the order information to a CSV file if the order is completed.

    The function use the PrepareOrder object to handle the current state of 
    the order process.

    Returns:
        None
"""
def main ():

    # Starting process - Step 1
    print ("Starting Application ....")
    print ("Reading database     ....")
    # Read csv file amd convert to a list of object cashiers instances
    list_cashiers=cashiers_read_list ()
    # Read csv file amd convert to a list of object customers instances
    list_customers=customers_read_list ()
    # Read csv files for allprpoducts and convert to a list of object customers instances
    list_products=products_read_list ()

    # Once the reading database information is correctly done 
    # Preparation a order starts - Step 2
    print ("Starting Preparation Order...")
    # Create a object PrepareOrder with the proper arguments recovered in the previous step
    info_list_order=PrepareOrder (list_cashiers, list_customers, list_products, True, False, False, False)
    # select a cashier for the order 
    cashier_ordering = select_cashier (info_list_order) 
    # select a customer for the order     
    customer_ordering = select_customer (info_list_order)

    # Start order - Step 3
    # Start object order with the customer and cashier selected
    if (info_list_order.preparing_order and info_list_order.input_cashier 
               and info_list_order.input_customer):
        # Create object Order
        current_order = Order(cashier_ordering, customer_ordering)
        # The list of products is shown
        print ('--------------')
        print ('STARTING ORDER')
        print ('--------------')          
        print_list (info_list_order.list_products)
        # Keep the time to save in final order
        time_ordering = info_list_order.get_current_datetime()
        select_products (info_list_order, current_order)

    # Show final order - Step 4
    if (info_list_order.input_cashier and info_list_order.input_customer and 
            info_list_order.preparing_order and info_list_order.input_products):
        # Show final order
        print ('-----------')
        print ('FINAL ORDER')
        print ('-----------')
        current_order.show()
        # Write some order information in a CSV
        # The information to save : DNI cashier / DNI Customer / datetime ordering / Total
        order_data = [current_order.cashier.dni, current_order.customer.dni, 
                     time_ordering.strftime("%Y-%m-%d %H:%M:%S"), round(current_order.calculateTotal(), 2)]
        # Save the inforamtion to the CSV file
        save_order_information_csv(order_data)
    else:
        print ("Finished process")
        print ("The current order is cancelled")

# If execute file : execute process  
if __name__ == "__main__":
    main()


