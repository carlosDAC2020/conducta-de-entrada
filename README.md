# sistema de archivos 
programa q simula un sistema simula un cli para manejar un sietema de archivos sencillo, este programa nos permitira realizar operaciones sencillas como busqueda, creacion, elimiacion y listado de archivos.

![](/images/example.jpeg)

##  Funcionamiento 
- **Uso de modulos:** Se hace uso de algunas librerias las cuales nos ayudan a partes del funcionamiento del script
```python
""" Importar el módulo os para interactuar con el sistema operativo 
(cambiar entre directorios y ejecutar comandos) """
import os  
""" Importar colorama para agregar color al texto en la consola """
from colorama import init, Fore, Back  
""" Importar datetime para trabajar con fechas y horas """
import datetime  
```
En el caso de `colorama` y `datetime` no son bibliotecas estándar, por lo que se necesita instalarlas por separado usando pip con los siguientes comandos:

        `$ pip install colorama`
        `$ pip install datetime`
            

- **Establecimiento de ruta de trabajo:** Esta parte del código se encarga de establecer la ruta inicial de trabajo y de seguimiento (`header_path`) dentro de un simulador de sistema de archivos. Primero, obtiene la ruta absoluta del directorio donde se encuentra el script en ejecución (`ruta_script`). Luego, cambia el directorio de trabajo actual al directorio `c` dentro de `ruta_script`. Finalmente, `header_path` se inicializa con la ruta raíz (`C:\`) que se utilizará como base para la navegación y seguimiento de la ubicación actual dentro del sistema simulado.
```python
# Obtener la ruta al directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# nos ubicamos en el directorio c que hara de directorio raiz 
os.chdir(os.path.join(ruta_script, "c"))

# ruta de ubicacion actual la cual se ira actualizando segun se mueva entre directorios 
header_path = "C:\\"
```
- **Funcion principal de ejecuion** Esta parte del código representa el bucle principal de la aplicación que simula un sistema de archivos. En cada iteración del bucle `while True`, se solicita al usuario que ingrese un comando. El comando ingresado se pasa a la función `command_identification` para su validación y ejecución. La variable `header_path` se utiliza para mostrar la ruta actual en la línea de comando simulada. El bucle se ejecuta continuamente hasta que el usuario decida salir de la aplicación. La sección `if __name__ == '__main__':` garantiza que este código se ejecute solo si el script se ejecuta directamente.
```python
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
```
- **Validacion y ejecucion de comandos:** Se define la función `command_identification` que se encarga de analizar y ejecutar los comandos ingresados por el usuario. Primero, divide el comando ingresado en sus partes individuales utilizando el espacio como separador. Luego, verifica si el primer elemento de la lista de instrucciones es `"cd"` para cambiar de directorio utilizando la función `change_directory`. Si el comando es `"dir"`, llama a la función `list_content_directory` para listar el contenido del directorio actual. Para cualquier otro comando, se ejecuta el comando directamente en el sistema operativo utilizando `os.system`.
```python
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
```
### funciones especiales
- **Cambio de directorio:** La función `change_directory` permite cambiar el directorio actual de trabajo en un simulador de consola. Primero, verifica si el comando contiene dos elementos, lo cual indicaría un comando `cd` seguido de un directorio. Si el directorio es `".."`, retrocede un nivel en la estructura de directorios, eliminando el último elemento de la ruta actual. En caso contrario, intenta cambiar al directorio especificado dentro de la misma carpeta, actualizando la ruta actual en consecuencia. Si el comando no tiene la estructura esperada, simplemente imprime la ruta actual.
```python
def change_directory(command):
    # Verifica si el comando tiene dos elementos (cd y el directorio)
    if len(command) == 2:
        # Si el directorio es '..', retrocede un nivel en la estructura de directorios
        if command[1] == "..":
            # comando 'cd ..´ --> ['cd','..']
            return_rout = header_path.split("\\") # 'C:\D3\D31\D312' --> ['C:','D3','D31','D312']
            # Verifica si se intenta ir más atrás del directorio 'raíz' C
            if return_rout[1] == "":
                print("Ruta especificada no encontrada")
            else:
                # Elimina el último elemento (directorio actual)
                return_rout.pop() # ['C:','D3','D31','D312'] --> ['C:','D3','D31']
                # Elimina el primer elemento (raíz)
                return_rout.pop(0) # ['C:','D3','D31'] --> ['D3','D31']
                # Une los elementos restantes en una ruta
                return_rout = "\\".join(return_rout) # ['D3','D31'] --> 'D3\D31'
                # Cambia al nuevo directorio
                os.chdir(os.path.join(ruta_script, "C", return_rout)) # -> ruta\script\C\D3\D31
                # Actualiza la ruta actual
                header_path = "C:\\" + return_rout # -> C:\D3\D31

        # Cambiar a un otro directorio
        else:
            # comando 'cd D31\D311´ --> ['cd','D31\D311']
            current_rout = header_path.split("\\") # 'C:\D3' --> ['C:','D3']
            # Elimina el primer elemento (raíz)
            current_rout.pop(0) # ['C:','D3'] --> ['D3'] 
            # Une los elementos restantes en una ruta
            current_rout = "\\".join(current_rout) # ['D3'] -> D3
            if os.path.isdir(os.path.join(ruta_script, "C", current_rout, command[1])):
                # Cambiar al directorio especificado si existe
                os.chdir(os.path.join(ruta_script, "C", current_rout, command[1])) # -  ruta\script\C\D3\D31\D311
                # Actualiza la ruta actual
                if current_rout == "":
                    # en caso de ser un directorior en la 'raiz' C
                    header_path = "C:\\" + command[1]
                else:
                    # esto en caso de ser algun subdirectorio
                    header_path = "C:\\" + current_rout + "\\" + command[1] # C:\D3\D31\D311

    else:
        # Imprime la ruta actual si el comando no tiene la estructura esperada
        print(header_path)
```
Se realiza una búsqueda a partir de la carpeta actual hacia algún subdirectorio de esta. Por ejemplo, si se está en la raíz `C:\` y se entra al directorio `D3`, se puede seguir recorriendo los directorios ubicados en `D3` y así sucesivamente. Sin embargo, la búsqueda en dirección ascendente para retroceder de directorio no está disponible en esta simulación.
<div>
    <h4>Recorrido valido</h4>
    <img src="/images/recorrido_disponible.jpeg" alt="Descripción de la imagen 1" style="width: 400px;">  
</div>
<div>
    <h4>Recorrido no valido</h4>    
    <img src="/images/recorrido_no_disponible.jpeg" alt="Descripción de la imagen 2" style="width: 400px;">
</div>

El comando `cd ..` está habilitado en esta simulación para retroceder un directorio por comando. Esto significa que puedes usar `cd ..` para retroceder un nivel en la estructura de directorios en tu simulación. Sin embargo, solo puedes retroceder un directorio a la vez. Por ejemplo, si estás en el directorio `C:\D3\D31`  y ejecutas `cd ..`, retrocederás al directorio `C:\D3`.

- **Listar contenido de un directorio:** La función `list_content_directory()` obtiene y muestra de manera detallada el contenido del directorio actual. Primero, obtiene la ruta actual y la lista de elementos en ese directorio. Luego, itera sobre cada elemento y determina si es un directorio o un archivo. Para cada elemento, muestra la fecha de creación, el tipo (DIR/FLE), el tamaño en bytes y el nombre. Finalmente, muestra un separador para indicar el final de la lista.
```python
def list_content_directory():
    # Obtiene la ruta actual separada por el separador de directorios
    current_rout = header_path.split("\\")
    # Elimina el primer elemento (raíz)
    current_rout.pop(0)  
    # Une los elementos restantes en una ruta
    current_rout = "\\".join(current_rout)  

    # Obtiene el contenido del directorio actual
    content = os.listdir(os.path.join(ruta_script, "C", current_rout))

    # Muestra el encabezado de la lista de contenido
    print('-'*55)
    print(Fore.MAGENTA+"\n{:20} {:10} {:10} {:10}".format('Created', 'Type', 'Size', 'Name')+Fore.RESET)
    print('-'*55)

    # Itera sobre el contenido del directorio
    for item in content:
        item_path = os.path.join(ruta_script, "C", current_rout, item)
        # Determina si el elemento es un directorio o un archivo
        type = Back.BLUE + "DIR" + Back.RESET if os.path.isdir(item_path) else Back.GREEN + "FLE" + Back.RESET
        # Obtiene el tamaño y la fecha de creación del elemento
        size = os.path.getsize(item_path)
        date_created_timestamp = os.path.getctime(item_path)
        date_created = datetime.datetime.fromtimestamp(date_created_timestamp).strftime("%d/%m/%Y %I:%M %p")
        # Muestra la información del elemento
        print("{:^20} {:^10} {:^15} {:^8}".format(date_created, type, f'{size} bytes', item))
    
    # Muestra el separador final
    print('-'*55)
```

- ***Otros comandos disponibles:**Los siguiente comandos funcionan tal cual como en el cmd de Windows, esto usando la funcion `os.system`.

| Comando                | Descripción                                |
| :--------------------- | :----------------------------------------- |
| `$ dir`                | Muestra el contenido del directorio.       |
| `$ mkdir [nombre_directorio]` | Crea un nuevo directorio.            |
| `$ rmdir [nombre_directorio]` | Elimina un directorio vacío.         |
| `$ del [archivo]`      | Elimina un archivo.                        |
| `$ copy [origen] [destino]` | Copia archivos de un lugar a otro.   |
| `$ move [origen] [destino]` | Mueve archivos de un lugar a otro.   |
| `$ ren [nombre_actual] [nuevo_nombre]` | Cambia el nombre de un archivo o directorio. |
| `$ type [archivo]`     | Muestra el contenido de un archivo de texto. |
| `$ echo [contenido] > [archivo]` | Crea un archivo y escribe contenido en él.       |
| `$ echo [contenido] >> [archivo]` | Añade contenido a un archivo existente.          |
| `$ start [archivo]` | Abre un archivo con el programa predeterminado.       |

**NOTA:** es probable que se puedan usar mas comandos de Windows con normalidad 
a parte de los anteriormente mencionados, los cuales ya eatn probados.

## Pasos de ejecucion para Windows 

- clonar el repositorio
- Crear un entorno virtual en la carpeta del repositorio (**RECOMENDABLE**) 
 
          `$ py -m venv venv`

- Activar el entorno virtual (**estar ubicado en la raiz del proyecto**) 

          `$ .\venv\scripts\activate`

- Instalar las dependencias del proyecto ubicadas en el archivo requierements.txt

         `$ pip install -r requirements.txt`

- ejecuta el script 

         `$ py main. py`
