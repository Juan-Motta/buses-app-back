# OVERIDE - Proyecto app gestion viajes

## Acerca de la app


Overide es una applicacion creada con el fin de poder gestionar la compra de pasajes de buses intermunicipales.

## Tecnologias utilizadas

La applicacion fue contruida usando las siguientes tecnologias:

* PostgreSQL
* Django
* VueJS

## Instalacion y configuracion

Una vez clonado el repositorio y creado el entorno virtual, se debe ingresar a la carpeta raiz y con el entorno virtual activado se debe ejecutar el comando

```console
pip install -r requirements.txt
```

El proyecto de desarrollo esta corriendo con PostgreSQL, se debe configurar la base de datos en el archivo local.py y configurar las credenciales de acceso.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
```
Si se desea hacer uso de sqlite3 se debe modifcar la variable DATABASES por.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Una vez se han realizado las configuraciones se debe ejecutar el comando en la misma carpeta que contiene el manage.py con el fin de realizar las migraciones a la base de datos

```console
python manage.py makemigrations
```

Una vez se han configurado las migraciones se deben implementar con el comando

```console
python manage.py migrate
```

Una vez configurada la base de datos se debe crear un superusuario para poder acceder al administrador

```console
python manage.py createsuperuser
```

**Si se desea limpiar la base de datos se deben eliminar los archivos dentro de las carpetas migrations excepto el __init__.py y eliminar el archivo db.sqlite3 dentro de la carpeta admin_rest**

Finalmente se puede ejecutar el servidor de desarrollo con el comando

```console
python manage.py runserver
```

## Servicios REST


### Administrador
```
http://localhost:8000/admin
```

### Rutas API - Usuarios

**Listar Usuarios**
```
http://localhost:8000/api/usuario/
```

**Listar Usuario**
```
http://localhost:8000/api/usuario/<str:documento>
```

**Crear usuario**
```
http://localhost:8000/api/usuario/<str:documento>
```

**Actualizar usuario**
```
http://localhost:8000/api/usuario/<str:documento>
```

**Eliminar usuario**
```
http://localhost:8000/api/usuario/<str:documento>
```

Formato JSON para crear y actualizar usuarios:
```JSON
{
	"name": "Jhon",
	"last_name": "Doe",
	"email": "jhon@example.com",
	"password": "miclave123",
	"document": "12345678",
	"birth": "2021-10-06",
	"phone": "12345678"
}
```

### Rutas API - Trayectos

**Listar Trayectos**
```
http://localhost:8000/api/trayecto/
```

**Listar Trayecto**
```
http://localhost:8000/api/trayecto/<int:id>
```

**Crear Trayecto**
```
http://localhost:8000/api/usuario/<int:id>
```

**Actualizar Trayecto**
```
http://localhost:8000/api/usuario/<int:id>
```

**Eliminar Trayecto**
```
http://localhost:8000/api/usuario/<int:id>
```

Formato JSON para crear y actualizar Trayectos:
```JSON
{
	"origen": "Bogota",
	"destino": "Medellin",
	"fecha": "2021-10-07",
	"hora": "18:00:00",
	"precio": 70000,
	"puestos": 30
}
```

### Rutas API - Reservas

**Listar Reservas**
```
http://localhost:8000/api/reserva/
```

**Listar Reserva**
```
http://localhost:8000/api/reserva/<int:id>
```

**Crear Reserva**
```
http://localhost:8000/api/reserva/<int:id>
```

**Actualizar Reserva**
```
http://localhost:8000/api/reserva/<int:id>
```

**Eliminar Reserva**
```
http://localhost:8000/api/reserva/<int:id>
```

Formato JSON para crear y actualizar Trayectos:
```JSON
{
	"id": 7,
	"usuario": 1,
	"trayecto": 1,
	"nombre": "Jhon",
	"apellido": "Doe",
	"documento": "12345678",
	"fecha_nacimiento": "2021-10-06",
	"telefono": "12345678",
	"puesto": 1
}
```

### Rutas API - Tokens

**Generar token**
```
http://localhost:8000/api/token/
```

Formato JSON para generar el token:
```JSON
{
	"username": "jhon123",
	"password": "12345678"
}
```

**Refrescar token**
```
http://localhost:8000/api/token/refresh/
```

## Notas

**0.1.0**  

* Cambios al diseño base del proyecto
* Agregada configuracion de postgres (controlador y conexion local en el archivo base.py)
* Agregados modelos de las apps personas, viajes, pasajeros, buses, trayectos y ciudades.
* Agregados modelos al administrador de Django

**0.1.1**

* Cambios en las apps del proyecto
* Agregadas configuraciones de visualizacion en el administrador
* Agregadas caracteristica de autoasignacion de valor de los campos codigo de acuerdo a la tabla y a sus valores principales

**0.2.0**

* Cambios a las apps del proyecto
* Agregadas nuevas configuraciones de visualizacion en el administrador
* Eliminadas apps exepto Usuarios el cual pasa a llamarse Users
* Agregada opcion de creacion de usuarios y superusuarios en el administrador
* Agregada opcion para subir imagen y asociarla a un usuario
* Agregados servicios REST para la aplicacion Users (ver users/api)

**0.2.1**

* Cambios a la app usuarios
* Hasheo de contraseñas de usuarios corregido en la creacion y modificacion de usuarios desde el administrador y desde las peticiones PUT y POST
* Modificadas las PK de las bases de datos

**0.3.0**

* Agregada la app trayectos
* Definidos los metodos GET

**0.4.0**

* Cambios en el diseño del proyecto
* Eliminadas todas las app excepto users

**0.4.1**

* Creadas dos nuevas apps trayectos y reservas
* Creados los modelos y el administrador de reservas y trayectos

**0.4.2**

* Agregada validacion de seleccion de numero de puesto desde el administrador

**0.4.3**

* Agregados servicios rest (GET, POST, PUT, DELETE) para el modelo Usuarios

**0.4.4** 

* Agregados servicios rest (GET, POST, PUT, DELETE) para el modelo Trayectos

**0.4.5**

* Agregados servicios rest (GET, POST, PUT, DELETE) para el modelo Reservas

**0.4.6**

* Agregada validaciones a los servicios rest (POST, PUT) para el modelo reservas, ahora no esposible realizar o actualizar una reserva con un puesto ya ocupado y no es posible seleccionar un numero de asiento que no este disponible en el bus.

**0.4.7**

* Actualizada estructura del proyecto para produccion
* Agregada ruta de documentacion publica

**0.4.8**

* Corregido bug critico que no permitia acceder al administrador

**0.5.0**

* Agregado sistema de autenticacion por token
* Definidas nuevas rutas para obtener y refrescar los tokens

**0.5.1**

* Actualizadas rutas asociadas a los endpoints

**0.5.2**

* Actualizado proyecto a version preeliminar de produccion
* Instaladas dependencias necesarias para realizar el despliegue de la app

**0.5.3**

* Actualizadas rutas users y reservas, ahora requieren autenticacion para realizar peticiones HTTP
* Actualizada ruta trayectos, ahora la ruta no requiere autenticacion y es posible realizar peticiones HTTP

**0.5.4**

* Actualizados permisos de las APIs users y trayectos

**0.5.5**

* Corregidos errores de la aplicacion reservas

**0.5.6**

* Habilitado CORS

**0.5.7**

* Cambio payload devuelto por el servidor al realizar autenticacion, ahora devuelve nombre de usuario y id de usuario

**0.5.8**

* Corregidos errores en users

**0.5.9**

* Cambios en la aplicacion users, ahora el endpoint para obtener un usuario recibe el id como parametro en vez del documento

**0.5.10**

*Actualizada aplicacion reservas, ahora al realizar una peticion tipo POST a la API, esta devuelve un mensaje junto con el id del registro en la base de datos

**0.5.11**

* Modificado serializer de la aplicación user, ahora se entrega el id del usuario

**0.5.12**

* Solucionado bug en el serializador de la app users que impedia crear un usuario correctamente
