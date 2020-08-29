# coding: utf-8
__author__ = 'CotherArt'

from os import mkdir, path, listdir
from shutil import move
from paths import *
from fileformats import *


def moverodir(f_name, backupdir=main_dir):
    archivo = str(main_dir) + '\\' + f_name
    if not path.exists(backupdir):
        mkdir(backupdir)
        print('Directorio creado {}'.format(backupdir))
    move(archivo, backupdir)
    print('{} movido'.format(f_name))


for f_name in listdir(main_dir):
    extension = f_name.split('.')

    if extension[-1] in text_formats:
        moverodir(f_name, txtdir)

    elif f_name.endswith('.exe') and f_name != 'editando-directorios.exe':
        moverodir(f_name, exedir)
    if extension[-1] in package_formats:
        moverodir(f_name, pkgdir)
    if extension[-1] in images_formats:
        moverodir(f_name, imgdir)
