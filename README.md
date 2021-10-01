# OVERIDE - Proyecto app gestion viajes

## Acerca de la app


Overide es una applicacion creada con el fin de poder gestionar la compra de pasajes de buses intermunicipales.
Esta aplicacion esta creada como proyecto para el ciclo 3 de MisionTic20222 y en su creacion participan los siguientes integrantes:

* Andrea Lorena Castro Manzano
* Brian Alexander Beltran Poveda
* Cristian Humberto Ladino Vivas
* Juan Andres Lopez Motta
* Luis Fabian Calderon Fontalvo 

## Tecnologias utilizadas

La applicacion fue contruida usando las siguientes tecnologias:

* PostgreSQL
* Django
* React

## Instalacion y configuracion

Una vez clonado el repositorio y creado el entorno virtual, se debe ingresar a la carpeta requirements y con el entorno virtual activado se debe ejecutar el comando

```console
pip install -r local.txt
```

Antes de ejecutar el servidor de desarrollo se debe iniciar el servidor de base de datos de postgreSQL.
Primero se debe ingresar al servidor de posgres con el comando:
```console
psql -h localhost -U postgres
```
Una vez ingresado se debe crear una base de datos con el comando
```console
CREATE DATABASE busesapp;
```
Luego crear un usuario con el comando:
```console
CREATE USER admin;
```
Luego ingresar a la base de datos creada con el comando:
```console
\c busesapp;
```
y por ultimo asignarle rol de administrador al usuario anteriormente creado con el comando:
```console
ALTER ROLE admin WITH PASSWORD 'admin';
```
Una vez realizados estos pasos la base de datos quedara creada correctamente, si los datos de configuracion han cambiado se debe modificar el archivo local.py del proyecto en server/settings/local.py

Una vez se han realizado las configuraciones se debe ejecutar el comando en la misma carpeta que contiene el manage.py con el fin de realizar las migraciones a la base de datos
```console
python manage.py makemigrations
```
Una vez se han configurado las migraciones se deben implementar con el comando
```console
python manage.py migrate
```
Finalmente se puede ejecutar el servidor de desarrollo con el comando
```console
python manage.py runserver
```



## Notas

0.1.0  

* Cambios al diseño base del proyecto
* Agregada configuracion de postgres (controlador y conexion local en el archivo base.py)
* Agregados modelos de las apps personas, viajes, pasajeros, buses, trayectos y ciudades.
* Agregados modelos al administrador de Django

0.1.1

* Cambios en las apps del proyecto
* Agregadas configuraciones de visualizacion en el administrador
* Agregadas caracteristica de autoasignacion de valor de los campos codigo de acuerdo a la tabla y a sus valores principales

