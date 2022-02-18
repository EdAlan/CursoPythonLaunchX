### Creacion de except por no encontrar archivo
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")

#if __name__ == '__main__':
#    main()

###############################################################################

### Creacion de except por no encontrar archivo o tambien por detectarlo como directorio
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except PermissionError:
#        print("Found config.txt but it is a directory, couldn't read it")

#if __name__ == '__main__':
#    main()

###############################################################################

### Creacion de except por no encontrar archivo, por detectarlo como directorio o por tener un pc con sobrecarga de trabajo en el terce except con multiples except's

#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")
#    except (BlockingIOError, TimeoutError):
#        print("Filesystem under heavy load, can't complete reading configuration file")

###############################################################################

### Tambien es posible nombrar la exception para imprimirla como variable con AS

#try:
#    open("mars.jpg")
#except FileNotFoundError as err:
#    print("got a problem trying to read the file:", err)

###############################################################################

### Finalmente se puede usar la funcion .errno para usar el ID del error e imprimir un mensaje diferente

try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")