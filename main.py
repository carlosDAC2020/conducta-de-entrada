import os

# Obtener la ruta al directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Cambiar al directorio deseado
os.chdir(os.path.join(ruta_script, "c"))

header_path = "C:\\"

def command_identification(command):
    command_instructions = command.split(" ")
    # cambiar de directorio
    if "cd" == command_instructions[0]:
        change_directory(command_instructions)
    # mostrar un archivo por consola
    elif "cat"==command_instructions[0]:
        pass
    else :
        os.system(command)
        
    
# for command cd 
def change_directory(command):
    global header_path
    if len(command) == 2:
        # retroceder entre directorios 
        if command[1] == "..":
            return_rout = header_path.split("\\")
            if return_rout[1]=="":
                print("Ruta especificada no encontrada")
            else:
                return_rout.pop()
                return_rout.pop(0)
                return_rout = "\\".join(return_rout)
                os.chdir(os.path.join(ruta_script, "C", return_rout))
                header_path = "C:\\"+return_rout

        # cambiar a un directorio en la misma carpeta 
        else:
            current_rout = header_path.split("\\")
            current_rout.pop(0)
            current_rout = "\\".join(current_rout)
            if os.path.isdir(os.path.join(ruta_script, "C", current_rout, command[1])):
                # Cambiar al directorio especificado si existe
                os.chdir(os.path.join(ruta_script, "C", current_rout, command[1]))
                # actualizamos la ruta actual
                if current_rout=="":
                    header_path = "C:\\"+command[1]
                else:
                    header_path = "C:\\"+current_rout+"\\"+command[1]

    else:
        print("en caso de usar banderas")
    
    
    pass

def delete_file(command):
    pass

def create_file(command):
    pass

def create_directory(command):
    pass

def delete_directory(command):
    pass

def run():
    while True:
        command = input(f"{header_path}> ")
        command_identification(command)

        
if __name__ == '__main__':
    run()






