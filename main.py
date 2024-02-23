# Importar el módulo os para interactuar con el sistema operativo (cambiar entre directorios y ejecutar comandos)
import os  
# Importar colorama para agregar color al texto en la consola
from colorama import init, Fore, Back  
 # Importar datetime para trabajar con fechas y horas
import datetime 

# Esta línea inicializa la biblioteca colorama para permitir el uso de colores en la consola
init()

# Obtener la ruta al directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# nos ubicamos en el directorio c que hara de directorio raiz 
os.chdir(os.path.join(ruta_script, "c"))

# ruta de ubicacion actual la cual se ira actualizando segun se mueva entre directorios 
header_path = "C:\\"

def command_identification(command):
    # obtenemos las instrucciones por ceparado del comando ingresado
    command_instructions = command.split(" ")
    # cambiar de directorio
    if "cd" == command_instructions[0]:
        change_directory(command_instructions)
    # listar directorios 
    elif "dir"==command_instructions[0]:
        list_content_directory()
        pass
    # demas comandos (start, del, type, cls, etc..)
    else :
        os.system(command)
        
    
def change_directory(command):
    global header_path
    # Verifica si el comando tiene dos elementos (cd y el directorio)
    if len(command) == 2:
        # Si el directorio es '..', retrocede un nivel en la estructura de directorios
        if command[1] == "..":
            return_rout = header_path.split("\\")
            # Verifica si se intenta ir más atrás del directorio 'raíz' C
            if return_rout[1] == "":
                print("Ruta especificada no encontrada")
            else:
                # Elimina el último elemento (directorio actual)
                return_rout.pop()  
                # Elimina el primer elemento (raíz)
                return_rout.pop(0)  
                # Une los elementos restantes en una ruta
                return_rout = "\\".join(return_rout)  
                # Cambia al nuevo directorio
                os.chdir(os.path.join(ruta_script, "C", return_rout))  
                # Actualiza la ruta actual
                header_path = "C:\\" + return_rout  

        # Cambiar a un directorio en la misma carpeta
        else:
            current_rout = header_path.split("\\")
            # Elimina el primer elemento (raíz)
            current_rout.pop(0)  
            # Une los elementos restantes en una ruta
            current_rout = "\\".join(current_rout)  
            if os.path.isdir(os.path.join(ruta_script, "C", current_rout, command[1])):
                # Cambiar al directorio especificado si existe
                os.chdir(os.path.join(ruta_script, "C", current_rout, command[1]))
                # Actualiza la ruta actual
                if current_rout == "":
                    # en caso de ser un directorior en la 'raiz' C
                    header_path = "C:\\" + command[1]
                else:
                    # esto en caso de ser algun subdirectorio
                    header_path = "C:\\" + current_rout + "\\" + command[1]

    else:
        # Imprime la ruta actual si el comando no tiene la estructura esperada
        print(header_path)


def list_content_directory():
    current_rout = header_path.split("\\")
    current_rout.pop(0)
    current_rout = "\\".join(current_rout)
    content = os.listdir(os.path.join(ruta_script, "C", current_rout))

    print('-'*55)
    print(Fore.MAGENTA+"\n{:20} {:10} {:10} {:10}".format('Created', 'Type', 'Size', 'Name')+Fore.RESET)
    print('-'*55)
    for item in content:
        item_path = os.path.join(ruta_script, "C", current_rout, item)
        type =  Back.BLUE + "DIR"+ Back.RESET if os.path.isdir(item_path) else Back.GREEN + "FLE"+ Back.RESET 
        size = os.path.getsize(item_path)
        date_created_timestamp = os.path.getctime(item_path)
        date_created = datetime.datetime.fromtimestamp(date_created_timestamp).strftime("%d/%m/%Y %I:%M %p")
        print("{:^20} {:^10} {:^15} {:^8}".format(date_created, type, f'{size} bytes', item))
    print('-'*55)
    

def run():
    while True:

        # estilos de linea de comando 
        aux = header_path.split("\\")
        raiz= Fore.CYAN + aux[0]
        ruta = "\\"+"\\".join(aux[1:]) 
        ruta = Fore.GREEN + ruta

        # ingreso de comandos 
        command = input(f" {raiz}{ruta}> "+Fore.MAGENTA+"$ "+Fore.WHITE)

        # validacion y ejecucion de comandos 
        command_identification(command)

        
if __name__ == '__main__':
    os.system('cls')
    run()






