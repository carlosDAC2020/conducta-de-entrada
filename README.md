# sistema de archivos 
programa q simula un sistema simula un cli para manejar un sietema de archivos sencillo, este programa nos permitira realizar operaciones sencillas como busqueda, creacion, elimiacion y listado de archivos.

![](/images/example.jpeg)

##  Funcionamiento 
- Se hace uso de algunas librerias las cuales nos ayudan a partes del funcionamiento del script
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
            

- Esta parte del código se encarga de establecer la ruta inicial de trabajo y de seguimiento (`header_path`) dentro de un simulador de sistema de archivos. Primero, obtiene la ruta absoluta del directorio donde se encuentra el script en ejecución (`ruta_script`). Luego, cambia el directorio de trabajo actual al directorio `c` dentro de `ruta_script`. Finalmente, `header_path` se inicializa con la ruta raíz (`C:\`) que se utilizará como base para la navegación y seguimiento de la ubicación actual dentro del sistema simulado.
```python
# Obtener la ruta al directorio actual del script
ruta_script = os.path.dirname(os.path.abspath(__file__))

# nos ubicamos en el directorio c que hara de directorio raiz 
os.chdir(os.path.join(ruta_script, "c"))

# ruta de ubicacion actual la cual se ira actualizando segun se mueva entre directorios 
header_path = "C:\\"
```

## Búsqueda
En esta función se simula la ejecución del comando `cd` para cambiar de directorio de varias formas.

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

## Otros comandos disponibles 
Los siguiente comandos funcionan tal cual como en el cmd de Windows 

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
