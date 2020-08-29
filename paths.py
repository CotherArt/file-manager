# coding: utf-8
__author__ = 'CotherArt'


from pathlib import Path
from os import getcwd


main_dir = getcwd()  # Carpeta de descargas
txtdir = Path(main_dir + '/Textos/')
exedir = Path(main_dir + '/Ejecutables/')
imgdir = Path(main_dir + '/Imagenes/')
pkgdir = Path(main_dir + '/Paquetes/')
