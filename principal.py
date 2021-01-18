# IMPORTACIONES
import os.path
import configparser

print(' ')
print('------------------------------------------------------------------------------------------')
print('-------------------------Bienvenido a Potome DayZ Change 1.07-------------------by.PotoBW-')
print('------------------------------------------------------------------------------------------')
print('-----------Este programa te permitirá cambiar el IP de conexión con el servidor-----------')
print('------------------------------------------------------------------------------------------')
print(' ')
a = True
c = '!Start_client_parameters.ini'
while (a):
    b = input('¿El nombre del archivo de configuración es '' + c + ''? ( s=si / n=no ):').lower()
    print(' ')
    if b == 'n':
        e = True
        while (e):
            c = input('Introduzca el nuevo nombre del archivo de configuración:  ').lower()
            print(' ')
            e = not os.path.isfile(c)
            a = False
    elif not b == 's':
        print('------------------------------------------------------------------------------------------')
        print('------------------------------░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█------------------------------')
        print('------------------------------░█▀▀▀ ░█▄▄▀ ░█▄▄▀ ░█──░█ ░█▄▄▀------------------------------')
        print('------------------------------░█▄▄▄ ░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█------------------------------')
        print('------------------------------------------------------------------------------------------')
        print(' ')
        print('Debes escribir ( s=si / n=no )')
        print(' ')
    else:
        a = False
d = configparser.ConfigParser()
d.read(c, encoding='utf-16')
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
with open(c, 'w', encoding='utf-16') as archivoconfig:
    d.write(archivoconfig)
archivoconfig.close()
print('------------------------------------------------------------------------------------------')
print('---------------------------Se ha editado con éxito el archivo-----------------------------')
print('----------------------------------Presione ENTER salir------------------------------------')
print('------------------------------------------------------------------------------------------')
input()
