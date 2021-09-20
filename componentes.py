import math
from datetime import *

from helpers import borrarPantalla, gotoxy
import time
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError): 
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError, col, fil):
        while True:
            gotoxy(col,fil); valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col,fil); print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(" "*80)
        return valor

    # https://parzibyte.me/blog/2020/04/23/validar-fecha-python/
    def fecha(self,mensaje,mensajeError, col, fil):
        while True:
            gotoxy(col,fil); fecha = str(input("          ------>   | {} ".format(mensaje)))
            try:
                fecha = datetime.strptime(fecha, '%Y-%m-%d')
                break
            except:
                gotoxy(col,fil); print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(" "*80)
        return fecha

    # http: // blog.espol.edu.ec / ccpg1001 / s2eva_it2008_t2 - validar - cedula - ecuatoriana /
    def cedula(self,mensaje,mensajeError, col, fil):
        while True:

            gotoxy(col,fil); cedula = str(input("          ------>   | {} ".format(mensaje))).strip()
            cedulaAux =cedula

            try:
                if cedula[0] != "0":
                    gotoxy(col,fil); print("          ------><  | {} ".format(mensajeError))
                    time.sleep(1)
                    gotoxy(col,fil);print(" "*80)
                else:
                    # sin ceros a la izquierda
                    nocero = cedula.strip("0")

                    cedula = int(nocero, 0)
                    verificador = cedula % 10
                    numero = cedula // 10

                    # mientras tenga números
                    suma = 0
                    while (numero > 0):

                        # posición impar
                        posimpar = numero % 10
                        numero = numero // 10
                        posimpar = 2 * posimpar
                        if (posimpar > 9):
                            posimpar = posimpar - 9

                        # posición par
                        pospar = numero % 10
                        numero = numero // 10

                        suma = suma + posimpar + pospar

                    decenasup = suma // 10 + 1
                    calculado = decenasup * 10 - suma
                    if (calculado >= 10):
                        calculado = calculado - 10

                    if (calculado == verificador):
                        validado = 1
                        break
                    else:
                        validado = 0
                        gotoxy(col,fil); print("          ------><  | {} ".format(mensajeError))
                        time.sleep(1)
                        gotoxy(col,fil);print(" "*80)   
            except:
                gotoxy(col,fil); print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(" "*80)
        return str(cedulaAux)


    
class otra:
    pass    

