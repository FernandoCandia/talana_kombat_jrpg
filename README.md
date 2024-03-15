#  Talana Kombat JRPG
 Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Pre-requisitos
-   Docker 25.0.3^

##  Instalación

### Alternativa 1 - DockerHub

Descarga la imagen Docker con el siguiente comando en consola:

```sh
docker pull fdojavier2/talana_kombat_jrpg:1.0.0
```

Luego debemos ejecutar el contenedor con:

```sh
docker run -it --rm -p 8000:80 fdojavier2/talana_kombat_jrpg:1.0.0
```

### Alternativa 2 - Archivo comprimido

Debes descomprimir el archivo 'talana_kombat_jrpg.zip', acceder a este directorio descomprimido desde la consola y ejecutar los siguientes comandos:

```sh
docker build -t talana_kombat_jrpg .
docker run -it --rm -p 8000:80 talana_kombat_jrpg
```

Luego en el explorador acceder a http://localhost:8000 y comenzar a ocupar la aplicación.

## Interacción con página web
Cargar archivo JSON con los ejemplos que aparecen en el mismo directorio del proyecto django o cualquier otro archivo JSON con el formato de entrada correspondiente.

En base a los datos de entrada en formato JSON se relatará la pelea y el resultado final.

## Tests

Mientras está corriendo el servidor, puedes ejecutar los tests del proyecto django con los siguientes comandos en una nueva consola en el root del proyecto (Importante: no debes terminar la ejecución el servidor en la consola anterior):

```sh
docker ps -q | Select-Object -Last 1 | ForEach-Object { docker exec -it $_ bash }
cd kombat/
pytest
```