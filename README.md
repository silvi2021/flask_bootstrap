# Documentación
Este es una aplicación web utilizando el framework flask y bootstrap. Su propósito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos postgres utilizando migraciones.

Las dependencias se gestionan con pinpenv.

## Dependencias
Para correr este proyecto usted necesita tener instalado python 3 y su herramienta pip.
Para revisar si las tiene instalado debe ejecutar los siguientes comandos:

```
python -V
pip -V
```

El resultado debe indicar un número superior a 3.
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar `pipenv install`

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:

```
flask db upgrade
```

En caso de modificar un modelo agregando o modificando un atributo,debemos generar una nueva migración con el comando

```
flask db migrate -m"mensaje de la migración"
```

**nota**: Los comandos anteriores se deben ejecutar dentro de `pipenv shell`

## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente

```
flask --app app --debug run
```


