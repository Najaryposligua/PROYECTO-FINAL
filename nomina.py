from componentes import Menu, Valida
from helpers import borrarPantalla, gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import date
import time


# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2); 
    print("MANTENIMIENTO DE EMPLEADOS ADMINISTRATIVOS")
    gotoxy(15, 5);print("Nombre Empleado Administraivo: ")
    gotoxy(15, 6);print("Sueldo Empleado Administraivo: ")
    gotoxy(15, 7);print("Fecha Ingreso Empleado Administraivo: ")
    gotoxy(15, 8);print("Cedula Empleado Administraivo: ")
    gotoxy(15, 9);print("Direccion Empleado Administraivo: ")
    gotoxy(15, 10);print("Telefono Empleado Administraivo: ")
    gotoxy(15, 11);print("Departamento Empleado Administraivo: ID [                    ] ")
    gotoxy(15, 12);print("Cargo Empleado Administraivo:        ID [                    ] ")
    gotoxy(55, 5); nombreEmpleadoAdministrativo = input()
    sueldoEmpleadoAdministrativo = validar.solo_decimales("Ingrese Sueldo","Error: Suelfdo no fue validada", 55, 6)
    fechaIngresoEmpleadoAdministrativo = validar.fecha("Ingrese Fecha en el formato YYYY-MM-DD","Error: Fecha no fue validada", 55, 7)
    cedulaEmpleadoAdministrativo = validar.cedula("Ingrese Cedula","Error: Cedula no fue validada", 55, 8)
    gotoxy(55, 9); direccionEmpleadoAdministrativo = input()

    telefonoEmpleadoAdministrativo = None
    while True:
        telefonoEmpleadoAdministrativo = validar.solo_numeros("Error: telefono no fue validada", 55, 10)
        if len(str(telefonoEmpleadoAdministrativo)) == 10:
            break
        else:
            gotoxy(55, 10);
            print("Error: telefono debe contener 10 digitos")
            time.sleep(1)
            gotoxy(55, 10);
            print(" " * 50)

    departamento, entDepartamento = [], None
    while not departamento:
        gotoxy(57, 11);
        id = input().upper()
        archiEmpleado = Archivo("./archivos/departamento.txt", "|")
        departamento = archiEmpleado.buscar(id)
        if departamento:
            entDepartamento = Departamento(departamento[1], departamento[0])
            gotoxy(57, 11);print(entDepartamento.descripcion)
        else:
            gotoxy(57, 11);print("No existe Departamento con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(57, 11);print(" " * 50)

    cargo, entCargo = [], None
    while not cargo:
        gotoxy(57, 12);
        id = input().upper()
        archiCargo = Archivo("./archivos/cargo.txt", "|")
        cargo = archiCargo.buscar(id)
        if cargo:
            entCargo = Cargo(cargo[1], cargo[0])
            gotoxy(57, 12);
            print(entCargo.descripcion)
        else:
            gotoxy(57, 12);
            print("No existe Cargo con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(57, 12);
            print(" " * 50)

        gotoxy(15, 9);
    
    gotoxy(15, 13);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 13);
    grabar = input().lower()
    if grabar == "s":
        archiEmpleadoAdministrativo = Archivo("./archivos/administrativo.txt", "|")
        empleadosAdministrativos = archiEmpleadoAdministrativo.leer()
        if empleadosAdministrativos:
            # idSig = int(empleadosAdministrativos[-1][0]) + 1
            cantidad = len(empleadosAdministrativos[-1][0])
            # Aki obtengo los ultimos numero y aumento + 1
            idSig = int(empleadosAdministrativos[-1][0][1:cantidad]) + 1
            idSig = "A{}".format(idSig)
        else:
            idSig = "A1"
            # idSig = 1
        empleadoAdministrativo = Administrativo(nombreEmpleadoAdministrativo, entDepartamento, entCargo,
                                                direccionEmpleadoAdministrativo, cedulaEmpleadoAdministrativo,
                                                telefonoEmpleadoAdministrativo,fechaIngresoEmpleadoAdministrativo,
                                                sueldoEmpleadoAdministrativo, idSig)
        datos = empleadoAdministrativo.getEmpleado()
        datos = '|'.join(datos)
        archiEmpleadoAdministrativo.escribir([datos], "a")
        
        gotoxy(10, 14);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 14);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def empObreros():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE EMPLEADOS OBRERO")
    gotoxy(15, 5);print("Nombre Empleado Obrero: ")
    gotoxy(15, 6);print("Sueldo Empleado Obrero: ")
    gotoxy(15, 7);print("Fecha Ingreso Empleado Obrero: ")
    gotoxy(15, 8);print("Cedula Empleado Obrero: ")
    gotoxy(15, 9);print("Direccion Empleado Obrero: ")
    gotoxy(15, 10);print("Telefono Empleado Obrero: ")
    gotoxy(15, 11);print("Departamento Empleado Obrero: ID [                    ] ")
    gotoxy(15, 12);print("Cargo Empleado Obrero:        ID [                    ] ")
    gotoxy(55, 5);nombreEmpleadoObrero = input()
    sueldoEmpleadoObrero = validar.solo_decimales("Ingrese Sueldo", "Error: Suelfdo no fue validada",55,6)
    fechaIngresoEmpleadoObrero = validar.fecha("Ingrese Fecha en el formato YYYY-MM-DD","Error: Fecha no fue validada",55,7)
    cedulaEmpleadoObrero = validar.cedula("Ingrese Cedula", "Error: Cedula no fue validada", 55,8)
    gotoxy(55, 9); direccionEmpleadoObrero = input()

    telefonoEmpleadoObrero = None
    while True:
        telefonoEmpleadoObrero = validar.solo_numeros("Error: telefono no fue validada", 55, 10)
        if len(str(telefonoEmpleadoObrero)) == 10:
            break
        else:
            gotoxy(55, 10);
            print("Error: telefono debe contener 10 digitos")
            time.sleep(1)
            gotoxy(55, 10);
            print(" " * 50)

    departamento, entDepartamento = [], None
    while not departamento:
        gotoxy(57, 11);
        id = input().upper()
        archiEmpleado = Archivo("./archivos/departamento.txt", "|")
        departamento = archiEmpleado.buscar(id)
        if departamento:
            entDepartamento = Departamento(departamento[1], departamento[0])
            gotoxy(57, 11);
            print(entDepartamento.descripcion)
        else:
            gotoxy(57, 11);
            print("No existe Departamento con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(57, 11);
            print(" " * 40)

    cargo, entCargo = [], None
    while not cargo:
        gotoxy(57, 12);
        id = input().upper()
        archiCargo = Archivo("./archivos/cargo.txt", "|")
        cargo = archiCargo.buscar(id)
        if cargo:
            entCargo = Cargo(cargo[1], cargo[0])
            gotoxy(57, 12);
            print(entCargo.descripcion)
        else:
            gotoxy(57, 12);
            print("No existe Cargo con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(57, 12);
            print(" " * 40)

    gotoxy(15, 13);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 13);
    grabar = input().lower()
    if grabar == "s":

        archiEmpleadoObrero = Archivo("./archivos/obrero.txt", "|")
        empleadosObreros = archiEmpleadoObrero.leer()
        if empleadosObreros:
            # idSig = int(empleadosObreros[-1][0]) + 1
            cantidad = len(empleadosObreros[-1][0])
            # Aki obtengo los ultimos numero y aumento + 1
            idSig = int(empleadosObreros[-1][0][1:cantidad]) + 1
            idSig = "O{}".format(idSig)
        else:
            idSig = "O1"
            # idSig = 1
        empleadoObreror = Obrero(nombreEmpleadoObrero, entDepartamento, entCargo,
                                                direccionEmpleadoObrero, cedulaEmpleadoObrero,
                                                telefonoEmpleadoObrero, fechaIngresoEmpleadoObrero,
                                                sueldoEmpleadoObrero, idSig)
        datos = empleadoObreror.getEmpleado()
        datos = '|'.join(datos)
        archiEmpleadoObrero.escribir([datos], "a")

        gotoxy(10, 14);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 14);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def cargos():
    borrarPantalla()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE CARGOS")
    gotoxy(15, 5);print("Descripcion Cargo: ")
    gotoxy(35, 5);desCargo = input()

    gotoxy(15, 6);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 6);
    grabar = input().lower()
    if grabar == "s":

        archiCargo = Archivo("./archivos/cargo.txt", "|")
        cargos = archiCargo.leer()
        if cargos:
            idSig = int(cargos[-1][0]) + 1
        else:
            idSig = 1
        cargo = Cargo(desCargo, idSig)
        datos = cargo.getCargo()
        datos = '|'.join(datos)
        archiCargo.escribir([datos], "a")

        gotoxy(10, 7);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 7);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def departamento():
    borrarPantalla()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE DEPARTAMENTOS")
    gotoxy(15, 5);print("Descripcion Departamento: ")
    gotoxy(54, 5);
    desDepartamento = input()

    gotoxy(15, 6);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 6);
    grabar = input().lower()
    if grabar == "s":

        archiDepartamento = Archivo("./archivos/departamento.txt", "|")
        departamentos = archiDepartamento.leer()
        if departamentos:
            idSig = int(departamentos[-1][0]) + 1
        else:
            idSig = 1
        departamento = Departamento(desDepartamento, idSig)
        datos = departamento.getDepartamento()
        datos = '|'.join(datos)
        archiDepartamento.escribir([datos], "a")

        gotoxy(10, 7);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 7);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def empresa():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE EMPRESA")
    gotoxy(15, 5);print("Direccion Empresa: ")
    gotoxy(15, 6);print("Telefono Empresa: ")
    gotoxy(15, 7);print("RazonSocial Empresa: ")
    gotoxy(15, 8);print("Ruc Empresa: ")
    gotoxy(55, 5); direccionEmpresa = input()
    telefonoEmpresa = None
    while True:
        telefonoEmpresa = validar.solo_numeros("Error: solo numeros", 55, 6)
        if len(str(telefonoEmpresa)) == 10:
            break
        else:
            gotoxy(55, 6);print("Error: telefono debe contener 10 digitos")
            time.sleep(1)
            gotoxy(55, 6);print(" " * 50)

    gotoxy(55, 7); razonSocialEmpresa = input()
    rucEmpresa = None
    while True:
        gotoxy(55, 8);rucEmpresa = input()
        if len(rucEmpresa) == 14 and rucEmpresa[10] == "-":
            break
        else:
            gotoxy(55, 8);print("Error: Ruc debe ser 14 digitos del cuál en la 11 posición debe ir un guión ejemplo 1305276908-001")
            time.sleep(1)
            gotoxy(55, 8);print(" " * 50)
    
    gotoxy(15, 9);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 9);
    grabar = input().lower()
    if grabar == "s":

        archiEmpresa = Archivo("./archivos/empresa.txt", "|")
        empresa = Empresa(razonSocialEmpresa, direccionEmpresa,telefonoEmpresa,rucEmpresa)
        datos = empresa.getEmpresa()
        datos = '|'.join(datos)
        archiEmpresa.escribir([datos], "a")

        gotoxy(10, 10);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 10);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

def parametros():
    borrarPantalla()
    validar = Valida()
    gotoxy(20, 2);
    print("MANTENIMIENTO DE PARAMETROS")
    gotoxy(15, 5);print("Iess Deduccion: ")
    gotoxy(15, 6);print("Comision Deduccion: ")
    gotoxy(15, 7);print("Antiguedad Deduccion: ")
    iessDeduccion = validar.solo_decimales("Ingrese iess","Error: iess no fue validada", 55, 5)
    comisionDeduccion = validar.solo_decimales("Ingrese comision","Error: comision no fue validada", 55, 6)
    antiguedadDeduccion = validar.solo_decimales("Ingrese antiguedad","Error: antiguedad no fue validada", 55, 7)
    
    gotoxy(15, 9);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 9);
    grabar = input().lower()
    if grabar == "s":

        archiEmpresa = Archivo("./archivos/deducciones.txt", "|")
        deduccion = Deduccion(iessDeduccion, comisionDeduccion,antiguedadDeduccion)
        datos = deduccion.getDeduccion()
        datos = '|'.join(datos)
        archiEmpresa.escribir([datos], "a")

        gotoxy(10, 10);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 10);
        input("Registro No fue Grabado\n presione una tecla para continuar...")

# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
    borrarPantalla()
    gotoxy(20, 2);
    print("INGRESO DE HORAS EXTRAS")
    empleado, entEmpleado = [], None
    aamm, h50, h100 = 0, 0, 0
    while not empleado:
        gotoxy(15, 5);
        print("Empleado ID[    ]: ")
        gotoxy(27, 5);
        id = input().upper()
        archiEmpleado = Archivo("./archivos/obrero.txt", "|")
        empleado = archiEmpleado.buscar(id)
        if empleado:
            entEmpleado = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                 empleado[7], empleado[8], empleado[0])
            gotoxy(35, 5);print(entEmpleado.nombre)
        else:
            gotoxy(27, 5);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(27, 5);print(" " * 40)

    gotoxy(15, 6);print("Periodo[aaaamm]")
    gotoxy(15, 7);print("Horas50:")
    gotoxy(15, 8);print("Horas100:")
    validar = Valida()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 6)
    # gotoxy(23,6);aamm = input()
    gotoxy(23, 7);
    h50 = input()
    gotoxy(24, 8);
    h100 = input()
    gotoxy(15, 9);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 9);
    grabar = input().lower()
    if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt", "|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos:
            idSig = int(sobretiempos[-1][0]) + 1
        else:
            idSig = 1
        sobretiempo = Sobretiempo(entEmpleado, aamm, h50, h100, True, idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos], "a")
        gotoxy(10, 10);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 10);
        input("Registro No fue Grabado\n presione una tecla para continuar...")


def prestamos():
    borrarPantalla()
    gotoxy(20, 2);
    print("INGRESO DE PRESTAMOS")
    empleado, entEmpleado = [], None
    aamm = 0
    while not empleado:
        gotoxy(15, 5);
        print("Empleado ID[                 ]: ")
        gotoxy(27, 5);
        id = input().upper()
        esogerObrero = False
        # VALIDACION DE ESCOJER TANTO OBRERO COMO ADMINISTRATIVO
        if id.find("O") >= 0:
            esogerObrero = True
            gotoxy(15, 6);
            print("Usted ha buscado EMPLEADO OBRERO")
            archiEmpleado = Archivo("./archivos/obrero.txt", "|")
        else:
            gotoxy(15, 6);
            print("Usted ha buscado EMPLEADO ADMINISTRATIVO")
            archiEmpleado = Archivo("./archivos/administrativo.txt", "|")

        empleado = archiEmpleado.buscar(id)
        if empleado:

            if esogerObrero:

                entEmpleado = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                     empleado[7], empleado[8], empleado[0])
            else:
                entEmpleado = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5],
                                             empleado[6],
                                             empleado[7], empleado[8], empleado[0])
            gotoxy(15, 7);
            print(entEmpleado.nombre)
        else:
            gotoxy(15, 6);
            print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);
            gotoxy(15, 6);
            print(" " * 40)

    gotoxy(15, 7);print("Periodo[aaaamm]")
    gotoxy(15, 8);print("Valor:")
    gotoxy(15, 9);print("Numero de Pagos:")
    gotoxy(15, 10);print("Saldo:")
    validar = Valida()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 7)
    valor = validar.solo_decimales("Ingrese Valor","Error del valor", 35, 8)
    numeroPagos = int(validar.solo_numeros("Error: Solo numeros", 35, 9))
    saldo = validar.solo_decimales("Ingrese Saldo", "Error del saldo", 35, 10)

    gotoxy(15, 11);
    print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54, 11);
    grabar = input().lower()
    if grabar == "s":
        archiPrestamo = Archivo("./archivos/prestamo.txt", "|")
        prestamos = archiPrestamo.leer()
        if prestamos:
            idSig = int(prestamos[-1][0]) + 1
        else:
            idSig = 1
        prestamo = Prestamo(entEmpleado, aamm, valor, numeroPagos, saldo, True, idSig)
        datos = prestamo.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos], "a")
        gotoxy(10, 12);
        input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10, 12);
        input("Registro No fue Grabado\n presione una tecla para continuar...")


# opciones de Rol de Pago
def rolAdministrativo():
    borrarPantalla()
    # Se ingresa los datos del rol a procesar
    gotoxy(20, 2);
    print("ROL ADMINISTRATIVO")
    aamm = 0
    gotoxy(15, 6);
    print("Periodo[aaaamm]")
    validar = Valida()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 6)
    gotoxy(15, 7);
    print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54, 7);
    grabar = input().lower()
    entEmpAdm = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt", "|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm:
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt", "|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]), float(deducciones[1]), float(deducciones[2]))
            # print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(), aamm)
            for empleado in ListaEmpAdm:
                # print(empleado)
                entEmpAdm = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                           empleado[7], float(empleado[8]), empleado[0])
                # print(entEmpAdm.nombre,entEmpAdm.sueldo)
                nomina.calcularNominaDetalle(entEmpAdm, entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt", "|")
            archiRol.escribir([datosCab], "a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt", "|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm + '|' + '|'.join(dt)
                archiDet.escribir([dt], "a")
            # imprimir rol

            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                         entEmpresa.ruc, "O B R E R O S")
            nomina.mostrarDetalleNomina()

    else:
        gotoxy(10, 10);
        input("Rol No fue Procesado\n presione una tecla para continuar...")

    input("               Presione una tecla continuar...")


def consultaRol():
    borrarPantalla()
    validar = Valida()
    # Se ingresa los datos del rol a Consultar
    gotoxy(20, 2);
    print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
    rol = 0
    aamm = ""
    gotoxy(15, 4);
    print("Obrero-Administrativo(O/A): ")
    gotoxy(15, 6);
    print("Periodo[aaaamm]")
    gotoxy(44, 4)
    rol = input().upper()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 6)
    gotoxy(15, 7);
    print("Esta seguro de consultar el Rol(s/n):")
    gotoxy(54, 7);
    procesar = input().lower()
    if procesar == "s":
        if rol == "A":
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt", "|")
        else:
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt", "|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1], cabrol[0])
            entCabRol.totIngresos = float(cabrol[2])
            entCabRol.totDescuentos = float(cabrol[3])
            entCabRol.totPagoNeto = float(cabrol[4])
            detalle = archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])
                # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                            entEmpresa.ruc, tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10, 10);
            input("No existe rol con ese periodo\n presione una tecla para continuar...")

    else:
        gotoxy(10, 10);
        input("Consulta Cancelada\n presione una tecla para continuar...")
    input("               Presione una tecla continuar...")


def rolObrero():
    borrarPantalla()
    # Se ingresa los datos del rol a procesar
    gotoxy(20, 2);
    print("ROL OBRERO")
    aamm = 0
    gotoxy(15, 6);
    print("Periodo[aaaamm]")
    validar = Valida()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 6)
    gotoxy(15, 7);
    print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54, 7);
    grabar = input().lower()
    entEmpAdm = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt", "|")
        ListaEmpObrero = archiEmp.leer()
        if ListaEmpObrero:
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt", "|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]), float(deducciones[1]), float(deducciones[2]))
            # print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(), aamm)
            for empleado in ListaEmpObrero:
                # print(empleado)
                entEmpAdm = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                           empleado[7], float(empleado[8]), empleado[0])
                # print(entEmpAdm.nombre,entEmpAdm.sueldo)
                nomina.calcularNominaDetalle(entEmpAdm, entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObr.txt", "|")
            archiRol.escribir([datosCab], "a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObr.txt", "|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado
            for dt in datosDet:
                dt = nomina.aamm + '|' + '|'.join(dt)
                archiDet.escribir([dt], "a")
            # imprimir rol

            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                         entEmpresa.ruc, "O B R E R O S")
            nomina.mostrarDetalleNomina()

    else:
        gotoxy(10, 10);
        input("Rol No fue Procesado\n presione una tecla para continuar...")

    input("               Presione una tecla continuar...")


def sobreEmpleado():
    borrarPantalla()
    validar = Valida()
    # Se ingresa los datos del rol a Consultar
    gotoxy(20, 2);
    print("CONSULTA - SOBRE DE EMPLEADO - DE UN EMPLEADO OBRERO - ADMINISTRATIVO")
    rol = 0
    aamm = ""
    gotoxy(15, 4);print("Obrero-Administrativo(O/A): ")
    gotoxy(15, 5);print("Periodo[aaaamm]")
    gotoxy(15, 6);print("Codigo Empleado [                ]")
    gotoxy(44, 4); rol = input().upper()
    aamm = validar.solo_numeros("Error: Solo numeros", 23, 5)

    empleado, entEmpleado = False, None
    while not empleado:
        gotoxy(33, 6);
        codigoEmpleado = input().upper()
        esogerObrero = False
        # VALIDACION DE ESCOJER TANTO OBRERO COMO ADMINISTRATIVO
        if codigoEmpleado.find("O") >= 0:
            esogerObrero = True
            archiEmpleado = Archivo("./archivos/obrero.txt", "|")
        else:
            archiEmpleado = Archivo("./archivos/administrativo.txt", "|")

        empleado = archiEmpleado.buscar(codigoEmpleado)
        if empleado:

            if esogerObrero:

                entEmpleado = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                     empleado[7], empleado[8], empleado[0])
                gotoxy(33, 7);
                print(entEmpleado.nombre)
                break
            else:
                entEmpleado = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5],
                                             empleado[6],
                                             empleado[7], empleado[8], empleado[0])
                gotoxy(33, 7);
                print(entEmpleado.nombre)
                break
               
        else:
            gotoxy(33, 6);
            print("No existe Empleado con ese codigo[{}]:".format(codigoEmpleado))
            time.sleep(2);
            gotoxy(33, 6);
            print(" " * 40)

    gotoxy(15, 8);
    print("Esta seguro de consultar el Rol(s/n):")
    gotoxy(55, 8);
    procesar = input().lower()

    if procesar == "s":
        if rol == "A":
            tit = "S O B R E - E M P L E A D O -  A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt", "|")
        else:
            tit = "S O B R E - E M P L E A D O - O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObr.txt", "|")
            archiRolDet = Archivo("./archivos/rolDetObr.txt", "|")
        cabrol = archiRolCab.buscar(aamm)

        if cabrol:
            entCabRol = Nomina(cabrol[1], cabrol[0])
            entCabRol.totIngresos = float(cabrol[2])
            entCabRol.totDescuentos = float(cabrol[3])
            entCabRol.totPagoNeto = float(cabrol[4])
            detalle = archiRolDet.buscarLista(aamm)
            for det in detalle:

                detaleNomina = det[1:]
                if detaleNomina[0] == codigoEmpleado:
                    entCabRol.detalleNomina.append(detaleNomina)


            entCabRol.mostrarDetalleNominaVertical(entEmpleado)
        else:
            gotoxy(10, 9);
            input("No existe rol con ese periodo\n presione una tecla para continuar...")

    else:
        gotoxy(10, 9);
        input("Consulta Cancelada\n presione una tecla para continuar...")
    input("               Presione una tecla continuar...")

# Menu Proceso Principal
opc = ''
while opc != '5':
    borrarPantalla()
    menu = Menu("Menu Principal", ["1) Mantenimiento", "2) Novedades", "3) Rol de Pago", "4) Consultas", "5) Salir"],
                20, 10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 != '7':
            borrarPantalla()
            menu1 = Menu("Menu Mantenimiento",
                         ["1) Empleados Administratvos", "2) Empleados Obreros", "3) Cargos", "4) Departamentos",
                          "5) Empresa", "6) Parametros", "7) Salir"], 20, 10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            if opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamento()
            elif opc1 == "5":
                empresa()
            elif opc1 == "6":
                parametros()

    elif opc == "2":
        borrarPantalla()
        menu2 = Menu("Menu Novedades", ["1) Sobretiempo", "2) Prestamos", "3) Salir"], 20, 10)
        opc2 = menu2.menu()
        if opc2 == "1":
            sobretiempos()
        elif opc2 == "2":
            prestamos()
    elif opc == "3":
        borrarPantalla()
        menu3 = Menu(
            "Menu Rol",
            ["1) Rol Administrativos", "2) Rol Obreros", "3) Consulta Rol", "4) Sobre Empleado", "5) Salir"],
            20,
            10
        )
        opc3 = menu3.menu()
        if opc3 == "1":
            rolAdministrativo()
        elif opc3 == "2":
            rolObrero()
        elif opc3 == "3":
            consultaRol()
        elif opc3 == "4":
            sobreEmpleado()
    elif opc == "4":
        borrarPantalla()
        menu4 = Menu("Menu Consultas",
                     ["1) Empleados", "2) Cargos", "3) Departamentos", "4) Empresa", "5) Parametros", "6) Salir"], 20,
                     10)
        opc4 = menu.menu()
    elif opc == "5":
        borrarPantalla()
        print("Gracias por su visita....")
    else:
        print("Opcion no valida")

input("Presione una tecla para salir")
borrarPantalla()
