""" 
Objetivo:
Sistema de Gestion de Productos
"""
import json

class Producto:
    def __init__(self, codigo, descripcion, rubro, precio, existencias):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__rubro = rubro
        self.__precio = self.validar_precio(precio)
        self.__existencias = self.validar_existencias(existencias)

    @property
    def codigo(self):
        return self.__codigo 
    
    @property     
    def descripcion(self):
        return self.__descripcion
    
    @property
    def rubro(self):
        return self.__rubro
    
    @property
    def precio(self):
        return self.__precio
    
    @property
    def existencias(self):
        return self.__existencias
    
    @precio.setter
    def precio(self,nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)

    @existencias.setter
    def existencias(self,nuevas_existencias):
        self.__existencias = self.validar_existencias(nuevas_existencias)    
    
    def to_dict(self):
        return {
            "codigo": self.codigo,
            "descripcion": self.descripcion,
            "rubro": self.rubro,
            "precio": self.precio,
            "existencias": self.existencias
        }
        
    def __str__(self):
        return f"{self.__codigo} {self.__descripcion}"
    def validar_precio(self,precio):
        try:
            precio = float(precio) 
            if precio < 0:
                raise ValueError("Precio debe ser no negativo")
            return precio
        except:
            raise ValueError("Precio es una variable numérica")
        
    def validar_existencias(self,existencias):
        try:
            stock = float(existencias)
            if stock < 0:
                raise ValueError("Las existencias deben ser no negativas")
            return stock
        except ValueError:
            raise ValueError("Existencias debe ser un valor numérico")
        
        
class ProductoCelular(Producto):
    def __init__(self, codigo, descripcion, rubro, precio, existencias, so, marca, modelo):
        super().__init__(codigo, descripcion, rubro, precio,existencias)
        self.__so = so
        self.__marca = marca
        self.__modelo = modelo

    @property
    def so(self):
        return self.__so
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def to_dict(self):
        """ return {
            "codigo": self.codigo,
            "descripcion": self.descripcion,
            "rubro": self.rubro,
            "precio": self.precio,
            "existencias": self.existencias,
            "sistema_operativo": self.so,
            "marca": self.marca,
            "modelo": self.modelo,
        } """
        data = super().to_dict()
        data["sistema_operativo"] = self.so
        data["marca"] = self.marca
        data["modelo"] = self.modelo
        return data 
        
    def __str__(self):
        return f"{super().__str__()} - Sistema Operativo: {self.__so} - Marca: {self.__marca}  - Modelo: {self.__modelo}"
    
class ProductoComputadora(Producto):
    def __init__(self, codigo, descripcion, rubro, precio, existencias, so, procesador):
        super().__init__(codigo, descripcion, rubro, precio,existencias)
        self.__so = so
        self.__procesador = procesador

    @property
    def so(self):
        return self.__so
    
    @property
    def procesador(self):
        return self.__procesador
    
    def to_dict(self):
        """ return {
            "codigo": self.codigo,
            "descripcion": self.descripcion,
            "rubro": self.rubro,
            "precio": self.precio,
            "existencias": self.existencias,
            "sistema_operativo": self.so,
            "marca": self.marca,
            "modelo": self.modelo,
        } """
        data = super().to_dict()
        data["sistema_operativo"] = self.so
        data["procesador"] = self.procesador
        return data 
        
    def __str__(self):
        return f"{super().__str__()} - Sistema Operativo: {self.__so} - Procesadora: {self.__procesador}"
        
class GestionProductos:
    def __init__(self,archivo):
       self.archivo = archivo
            
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
              datos = json.load(file)  
        except FileNotFoundError:    
            return {}
        except Exception as error:
            raise Exception(f"Error al leer el archivo {error}")
        else:
            return datos
                
    def guardar_datos(self,datos):
        try:
            with open(self.archivo,'w') as file:
                 json.dump(datos, file, indent=4)
        except IOError:
            print(f"error en la operacion de guardar datos en {self.archivo}")    
        except Exception as error:
            print(f"Se ha producido el siguiente error {error}")
                
    def crear_producto(self,producto):
        try:
            datos = self.leer_datos()
            codigo = producto.codigo
            if not(str(codigo)) in datos.keys():
                datos[codigo] = producto.to_dict()
                self.guardar_datos(datos)
                print(f"Se guardaron con éxito los datos")
            else:
                print(f"El producto ya existe en archivo")    
        except Exception as error:
            print(f"Se produjo el error {error} al intentar crear el producto")
                
    def leer_producto(self,codigo):
        try:
            datos = self.leer_datos()
            if codigo in datos:
                producto_data = datos[codigo]
                print(f"Producto encontrado: {producto_data}")   
                return producto_data   
            else:
                print(f"Producto No encontrado, codigo Solicitado {codigo}")  
                return {} 
        except Exception as error:
            print(f"Error al leer datos {error } producto: {codigo}")
            
    def actualizar_producto(self,codigo,producto):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                datos[codigo]= producto.to_dict()
                self.guardar_datos(datos)
                print(f"precio actualizado exitosamente producto {codigo}")
            else:
                print(f"no se econtro el producto con codigo {codigo}")    
        except Exception as error:
            print(f"Error al intentar actualizar precio del producto con codigo {codigo}")                            
            
    def actualizar_precio_producto(self,codigo,n_precio):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                datos[codigo]['precio'] = n_precio
                self.guardar_datos(datos)
                print(f"precio actualizado exitosamente producto {codigo}")
            else:
                print(f"no se econtro el producto con codigo {codigo}")    
        except Exception as error:
            print(f"Error al intentar actualizar precio del producto con codigo {codigo}")                            
            
    def actualizar_stock_producto(self,codigo,existencia):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                datos[codigo]['existencias'] = existencia
                self.guardar_datos(datos)
                print(f"precio actualizado exitosamente producto {codigo}")
            else:
                print(f"no se econtro el producto con codigo {codigo}")    
        except Exception as error:
            print(f"Error al intentar actualizar precio del producto con codigo {codigo}")     
                                           
    def eliminar_producto(self,codigo):
        try:
            datos = self.leer_datos()
            if str(codigo) in datos.keys():
                del datos[codigo]
                self.guardar_datos(datos)
                print(f"El Producto con codigo {codigo} ha sido eliminado exitosamente")
            else:
                print(f"No se encontro el producto con el codigo {codigo}")     
        except Exception as error:
                print(f"Error {error} al intentar acceder a datos de {codigo}")