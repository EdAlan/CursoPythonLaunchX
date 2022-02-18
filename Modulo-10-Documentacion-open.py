### Apertura de un archivo con error de que no encuentra el directorio y archivo mencionado
# open("/path/to/mars.jpg")

###############################################################################

### Intento de apertura de un archivo que nuevamente no se encuentra y genera la excepcion FileNotFoundError
#def main():
#    open("/path/to/mars.jpg")

#if __name__ == '__main__':
#    main()

###############################################################################

### Uso de Try y Except para tratar la falla del FileNotFoundError
try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")