# sistema de archivos 
programa q simula un sistema simula un cli para manejar un sietema de archivos sencillo, este programa nos permitira realizar operaciones sencillas como busqueda, creacion, elimiacion y listado de archivos.

![](/images/example.jpeg)

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
| `$ cd [directorio]`    | Cambia al directorio especificado.         |
| `$ cd..`               | Retrocede un nivel en la estructura de directorios. |
| `$ mkdir [nombre_directorio]` | Crea un nuevo directorio.            |
| `$ rmdir [nombre_directorio]` | Elimina un directorio vacío.         |
| `$ del [archivo]`      | Elimina un archivo.                        |
| `$ copy [origen] [destino]` | Copia archivos de un lugar a otro.   |
| `$ move [origen] [destino]` | Mueve archivos de un lugar a otro.   |
| `$ ren [nombre_actual] [nuevo_nombre]` | Cambia el nombre de un archivo o directorio. |
| `$ type [archivo]`     | Muestra el contenido de un archivo de texto. |

