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
    print(f"4- Actualizar producto")
    print(f"5- Baja producto a través de DNI")
    print(f"6- Mostrar todos los productos")
    print(f"9- Salir del sistema")
    print(f"")
    print(f"")
    print(f"---------------------------------------------------------")
    
def agregar_producto(gestion,opcion_producto):
    try:
        codigo = input("Código del producto:")
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
            
        gestion.crear_producto(producto)
    
    except ValueError as error:
        print(f"Ha sucedido un error: {error}")
    except Exception as error:
        print(f"Se produjo el siguiente error: {error}")    
    finally:
        input(f"presione una tecla para continuar")    
        
def buscar_producto_codigo(gestion):
    codigo = input(f"Ingrese código a buscar:")
    gestion.leer_producto(codigo)
    input(f"presione una tecla para continuar")
    
def mostrar_productos(gestion):
    print(f"Listado de Productos existentes")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for producto in gestion.leer_datos().values():
        if "procesador" in producto:
            print(f"Computadora: {producto['descripcion']} -SO: {producto["sistema_operativo"]} - Procesador: {producto["procesador"]}")
        else:
            print(f"Telefono {producto["descripcion"]} -Precio:{producto["precio"]} -SO: {producto['sistema_operativo']} -Marca: {producto["marca"]} -Modelo: {producto["modelo"]}")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    input("Presione una tecla para continuar")             
    
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
        elif opcion == '6':
            mostrar_productos(gestion)
                 
        elif opcion == '9':
            print(f"Fin del programa")
            break
        else:
            print(f"Opción inexistente. Seleccione una opción válida")
            input("presione enter para continuar")