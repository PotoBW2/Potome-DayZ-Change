# IMPORTACIONES
import os.path
import configparser

print(' ')
print('------------------------------------------------------------------------------------------')
print('-------------------------Bienvenido a Potome DayZ Change 1.07-------------------by.PotoBW-')
print('------------------------------------------------------------------------------------------')
print('-----Este programa te permitirá cambiar las configuraciones del "Launcher" del juego------')
print('------------------------------------------------------------------------------------------')
print(' ')
valNombre = True #variable para validar el nombre del archivo
#Cargamos el nombre guardado por primera vez en config
config = configparser.ConfigParser()
config.read("PDC/config.ini")
nombreArchivo = config['archivo']['nombre']
print('-------------------------------------------------------------------------------------------')
print('- Todos los archivos de este programa deben estar en la raíz del juego de lo contrario no -')
print('- funcionará, si no es asi por favor cierre la consola y copie los archivos en el lugar   -')
print('- correcto.                                                                               -')
print('-------------------------------------------------------------------------------------------')
print(' ')
#Empezamos a validar el nombre
while (valNombre):
    siNo = input('¿El nombre del archivo de configuración es -- ' + nombreArchivo + ' --? ( s=si / n=no ):').lower()#introducimos un si o un no para saber si el nombre cambia
    print(' ')
    if siNo == 'n':#Si es no introducimos un nombre nuevo
        valNewNombre = True#Validador de que el nuevo nombre exista
        while (valNewNombre):#repite la pregunta si el nuevo nombre no existe
            nombreArchivo = input('Introduzca el nuevo nombre del archivo de configuración:  ').lower()#introduciomos el nuevo nombre
            print(' ')
            valNewNombre = not os.path.isfile(nombreArchivo)#comprobar si existe el archivo
            valNombre = False#cerrar el while
        #guardar el nuevo nombre
        config['archivo']['nombre'] = nombreArchivo
        with open("PDC/config.ini", 'w') as archivoconfig:
            config.write(archivoconfig)
        archivoconfig.close()

    elif not siNo == 's':#lanzar en error en caso de no haber puesto un s para si o una n para no
        print('------------------------------------------------------------------------------------------')
        print('------------------------------░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█------------------------------')
        print('------------------------------░█▀▀▀ ░█▄▄▀ ░█▄▄▀ ░█──░█ ░█▄▄▀------------------------------')
        print('------------------------------░█▄▄▄ ░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█------------------------------')
        print('------------------------------------------------------------------------------------------')
        print(' ')
        print('Debes escribir ( s=si / n=no )')
        print(' ')
    else:
        valNombre = False#cerrar el while del nombre del archivo

d = configparser.ConfigParser()
d.read(nombreArchivo, encoding='utf-16')
f = d['Launcher']['CommandLine']
print('------------------------------------------------------------------------------------------')
print('---------------------------El archivo a sido cargado con éxito----------------------------')
print('------------------------------------------------------------------------------------------')
print(' ')
g = f.find('-connect=') + 9
h = f[g:f[g:].find(' ') + g]
print('------------------------------------------------------------------------------------------')
i = input('Su IP actual es: -' + h + '- , lo va a cambiar por: --> ')
print('------------------------------------------------------------------------------------------')
print(' ')
f = f.replace(h, i)
d['Launcher']['CommandLine'] = f
with open(nombreArchivo, 'w', encoding='utf-16') as archivoconfig:
    d.write(archivoconfig)
archivoconfig.close()
print('------------------------------------------------------------------------------------------')
print('---------------------------Se ha editado con éxito el archivo-----------------------------')
print('----------------------------------Presione ENTER salir------------------------------------')
print('------------------------------------------------------------------------------------------')
input()
