# coding: utf-8
__author__ = 'CotherArt'

from sys import exit
from os import mkdir, path, listdir
from os import getcwd
from pathlib import Path
from shutil import move
from fileformats import *

main_dir = getcwd()

# Move a file to an specific directory
def moverodir(f_name, backupdir=main_dir):
    archivo = str(main_dir) + '\\' + f_name
    if not path.exists(backupdir):
        mkdir(backupdir)
        print('Directorio creado {}'.format(backupdir))
    move(archivo, backupdir)
    print('{} movido'.format(f_name))

# Ask for the folder to manage
print("Wich forlder do you want to sort? type the route or press Enter to use the current directory.")
path_to_manage = input('>')
if len(path_to_manage) != 0:
    main_dir = path_to_manage

txtdir = Path(main_dir + '/Textos/')
exedir = Path(main_dir + '/Ejecutables/')
imgdir = Path(main_dir + '/Imagenes/')
pkgdir = Path(main_dir + '/Paquetes/')
viddir = Path(main_dir + '/Videos/')
offddir = Path(main_dir + '/Office/')

files_count = 0
for f_name in listdir(main_dir):
    print(f_name)
    files_count += 1

print('/n{} files to move. Do you want to continue? (y/n).'.format(files_count))
yesno = input('>')
# Continue or aabort the sorting
if yesno.lower() in ['n','no']:
    exit()

for f_name in listdir(main_dir):
    # Obtain the extension of the file
    extension = f_name.split('.')[-1]
    
    if extension in text_formats:
        moverodir(f_name, txtdir)
    if extension in exe_formats:
        moverodir(f_name, exedir)
    if extension in package_formats:
        moverodir(f_name, pkgdir)
    if extension in images_formats:
        moverodir(f_name, imgdir)
    if extension in exe_formats:
        moverodir(f_name, exedir)
    if extension in office_formats:
        moverodir(f_name, offddir)


