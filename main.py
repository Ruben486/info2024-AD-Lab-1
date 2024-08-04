import os
import platform
from productos_py_poo import (
    ProductoCelular,
    ProductoComputadora,
    GestionProductos
)
def clear_pantalla():
    '''Limpiar pantalla del SO'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') 
        
def menu_sistema():
    print(f"---------------------------------------------------------")
    print(f"---------------Menu de Sistema de Productos--------------")
    print(f"")
    print(f"1- Agregar Producto Teléfono Móvil")
    print(f"2- Alta producto computadora")
    print(f"3- Buscar producto por Código")
    print(f"4- Actualizar precio de producto")
    print(f"5- Baja producto a través de Codigo")
    print(f"6- Mostrar todos los productos")
    print(f"7- Actualizar existencias de producto")
    print(f"8- Actualizar producto")
    print(f"9- Salir del sistema")
    print(f"")
    print(f"")
    print(f"---------------------------------------------------------")
    
def pausa_display():    
    input(f"Presione una tecla para continuar ->: ")
    
def entrada_de_datos(codigo,opcion_producto,operacion):
    if operacion == "A":
       codigo = input("Código del producto: ")

    descripcion = input( "ingrese descripción: ")
    rubro = input("Ingrese Rubro del producto: ")   
    precio = input("Ingrese precio del producto: ")
    existencias = input("Ingrese existencia del producto: ")
        
    if opcion_producto == '1':
        so = input("Ingrese SO del producto: ")
        marca = input("Ingrese marca del producto: ")
        modelo = input("Ingrese modelo del producto: ")
        producto = ProductoCelular(codigo,descripcion,rubro,precio,existencias,so,marca,modelo)
        
            
    elif opcion_producto == '2':
        so = input("Ingrese SO del computador:")
        procesador = input("Ingrese Procesador del computador:")
        producto = ProductoComputadora(codigo,descripcion,rubro,precio,existencias,so,procesador)    
    return producto        

def agregar_producto(gestion,opcion_producto):
    try:
        producto = entrada_de_datos('',opcion_producto,'A')
        """     codigo = input("Código del producto:")
        descripcion = input("Ingrese descripción del producto:")
        rubro = input("Ingrese Rubro del producto:")
        precio = input("Ingrese precio del producto:")
        existencias = input("Ingrese existencia del producto:")
        
        if opcion_producto == '1':
            so = input("Ingrese SO del producto:")
            marca = input("Ingrese marca del producto:")
            modelo = input("Ingrese modelo del producto:")
            producto = ProductoCelular(codigo,descripcion,rubro,precio,existencias,so,marca,modelo)
            
        elif opcion_producto == '2':
            so = input("Ingrese SO del computador:")
            procesador = input("Ingrese Procesador del computador:")
            producto = ProductoComputadora(codigo,descripcion,rubro,precio,existencias,so,procesador)    
        else:
            print(f"opción inválida")
            input("presione enter para continuar")
        """        
        gestion.crear_producto(producto)
        print(f"Alta de producto ejecutada exitosamente")
        
    except ValueError as error:
        print(f"Ha sucedido un error: {error}")
    except Exception as error:
        print(f"Se produjo el siguiente error: {error}")    
    finally:
        pausa_display()
        
def actualizar_producto(gestion):        
    try:
        codigo = input(f"ingrese el código del producto a actualizar: ")
        producto = gestion.leer_producto(codigo)
        if "procesador" in producto:
            print(f"El producto es una computadora")
            producto = entrada_de_datos(codigo,"2","M")
        elif "marca" in producto:
            print(f"el producto es un móvil")    
            producto = entrada_de_datos(codigo,"1","M")
        
        continuar = input(f"Presione Enter para continuar, c-para cancelar: ")
        if continuar == 'c':
            print(f"Se canceló la modificación del producto")
        else:
            print(f"{codigo}")
            gestion.actualizar_producto(codigo,producto)
            print(f"Actualización de producto exitosa")
    except Exception as error:
        print(f"Se ha producido un error durante la actualizacion {error}")     
    pausa_display()
    
def buscar_producto_codigo(gestion):
    codigo = input(f"Ingrese código a buscar:")
    gestion.leer_producto(codigo)
    pausa_display()
    
def mostrar_datos_comunes(producto):
    print(f"-Descripción: {producto['descripcion']} -Precio: {producto["precio"]} -Existencias: {producto['existencias']} -SO: {producto["sistema_operativo"]}")
        
def mostrar_productos(gestion):
    print(f"Listado de Productos existentes")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for producto in gestion.leer_datos().values():
        if "procesador" in producto:
            print(f"Computadora: -Código: {producto["codigo"]}")
            mostrar_datos_comunes(producto)      
            print(f"-Procesador: {producto["procesador"]} \n")
        else:
            print(f"Teléfono -Codigo: {producto["codigo"]}")
            mostrar_datos_comunes(producto)
            print(f"-Marca: {producto["marca"]} \n-Modelo: {producto["modelo"]} \n")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    pausa_display()
    
def actualizar_precio_producto(gestion):
    codigo = input(f"ingrese codigo de Producto: ")
    producto = gestion.leer_producto(codigo)
    if "codigo" in producto:
        precio = float(input(f"Ingrese nuevo precio del producto: "))
        gestion.actualizar_precio_producto(codigo,precio)
        print(f"Se ha actualizado el precio del producto")
    else:
        print(f"El código ingresado no existe")  
    pausa_display()
    
def baja_producto(gestion):
    codigo = input(f"ingrese el codigo del producto a eliminar: ")
    gestion.eliminar_producto(codigo)
    pausa_display()
    
def actualizar_existencia_producto(gestion):
    codigo = input(f"ingrese el codigo del producto a actualizar: ")
    producto = gestion.leer_producto(codigo) 
    if "codigo" in producto:
       existencia = input(f"Ingrese nuevas existencias del producto: ")  
       gestion.actualizar_stock_producto(codigo,existencia)
       print(f"Existencia de producto actualizado exitosamente")
    else:
       print(f"El codigo ingresado no existe")   
    pausa_display()
    
if __name__ == '__main__':
    archivo_producto = "productos.json"
    gestion = GestionProductos(archivo_producto)
    
    while True:
        clear_pantalla()
        menu_sistema()
        opcion = input("seleccione una opción->: ")
        if opcion == '1' or opcion == '2':
            agregar_producto(gestion,opcion) 
        elif opcion == '3':
            buscar_producto_codigo(gestion)  
        elif opcion == '4':
            actualizar_precio_producto(gestion)    
        elif opcion == '5':
            baja_producto(gestion)    
        elif opcion == '6':
            mostrar_productos(gestion)
        elif opcion == '7':
            actualizar_existencia_producto(gestion)   
        elif opcion == '8':
            actualizar_producto(gestion)     
        elif opcion == '9':
            print(f"Fin del programa")
            break
        else:
            print(f"Opción inexistente. Seleccione una opción válida")
            pausa_display()