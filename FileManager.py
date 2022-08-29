# coding: utf-8
__author__ = 'CotherArt'

from sys import exit
from os import mkdir, path, listdir
from os import getcwd
from pathlib import Path
from shutil import move
from colorama import init, Fore, Back, Style
init() # init for colorama

main_dir = ''
formats = {}

# Move a file to an specific directory
def move_to_dir(f_name, backupdir):
    backupdir = main_dir + backupdir
    archivo = str(main_dir) + '\\' + f_name
    if not path.exists(backupdir):
        mkdir(backupdir)
        print(Fore.YELLOW + 'Directory created {}'.format(backupdir) + Fore.RESET)
    move(archivo, backupdir)
    print(Fore.CYAN + f_name + Fore.YELLOW + ' moved to -> ' + backupdir + Fore.RESET)

# --------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print(Fore.YELLOW + '''
███████╗██╗██╗     ███████╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
██╔════╝██║██║     ██╔════╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
█████╗  ██║██║     █████╗      ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██╔══╝  ██║██║     ██╔══╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║     ██║███████╗███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝''')
    # print(Fore.CYAN)
    print(Fore.CYAN + '\tBy:CotherArt')
    print('\thttps://github.com/CotherArt/file-manager.git')
    print(Fore.RESET)
    
    # Ask for the folder to manage
    main_dir = ''
    while len(main_dir) == 0:
        print(Fore.GREEN + "Which folder do you want to sort?" + Fore.RESET)
        main_dir = input('>')
        
    print(Fore.YELLOW + '\nScanning files at -->[{}]\n'.format(main_dir) + Fore.RESET)

    # Display and count the number or files at the main directory
    files_count = 0
    for f_name in listdir(main_dir):
        # Print files and directories in diferent colors
        if '.' in f_name:
            print(Fore.CYAN + f_name + Fore.RESET)
            files_count += 1
        else:
            print(f_name + Fore.RESET)
    
    yesno = ''
    while yesno not in ['y','yes','n','no']:
        print(Fore.YELLOW + '\n{}'.format(files_count) +Fore.GREEN+' files to move. Do you want to continue? (y/n).' + Fore.RESET)
        yesno = input('>')
        yesno = yesno.lower()
        # Continue or aabort the sorting
        if yesno in ['n','no']:
            exit()

    # Remove spaces from a given string
    def clean_spaces(string_input): 
        return string_input.replace(" ", "") 

    # parse the settings on the config.txt file
    with open('config.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            # Get rid of the enter char (\n)
            line = line.strip()
            line = clean_spaces(line)

            lista = line.split(':')
            lista2 = lista[1].split(',')
            formats['\\'+lista[0]] = lista2
    
    print('\n----------------------------------------------------------\n')
    # Get the file names from the main_dir
    for f_name in listdir(main_dir):
        # Obtain the extension of the file
        extension = f_name.split('.')[-1]
        
        # Move the files that matches with the config.txt file to their respective folder
        for f in formats:
            if extension in formats[f]:
                move_to_dir(f_name, f)

