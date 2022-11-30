# Documentación
Este es una aplicación web utilizando el framework flask y bootstrap. Su propósito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos postgres utilizando migraciones.

Las dependencias del proyecto se gestionan con pinpenv.

## Dependencias
Para correr este proyecto usted necesita tener instalado python 3 y su herramienta pip.
Para revisar si las tiene instalado debe ejecutar los siguientes comandos:

```
python -V
pip -V
```

El resultado debe indicar un número superior a 3.
Luego de clonar el repositorio, y para instalar las dependencias debe ejecutar el comando `pipenv install`

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:
Para ejecutar hacia adelante
```
flask db upgrade
```

Para ejecutar hacia atrás
```
flask db downgrade
```

Cuando hacemos un cambio en el modelo y necesitamos considerar esos cambios tambien en la base de datos,hay que generar una nueva migración.

```
flask db migrate -m"mensaje de la migración"
```

En caso de modificar un modelo agregando o modificando un atributo,debemos generar una nueva migración con el comando

```
flask db migrate -m"mensaje de la migración"
```

**nota**: Los comandos anteriores se deben ejecutar dentro de `pipenv shell`

## Blueprint

Los blueprint nos permiten componer aplicaciones desde componentes pequeños.Cada
componentes es como una mini aplicación.Permiten crear aplicaciones grandes,pero manteniendo el codigo y la estructura simples.

## Módulos

Para que los blueprint esten bien organizados, es mejor trabajarlos como módulos, es decir, que esten dentro de una carpeta,los módulos se pueden anidar,de echo,nosotros hicimos el módulo `app` con su respectivo `__init__.py` y dentro tenemos otros módulos como el módulo `messages` que es además un blueprint.

## Tarea 
Crear un nuevo recurso sencillo, sin base de datos,como blueprint bajo a
url`/memes` y debe renderiar un html lleno de memes


## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente

```
flask --app app --debug run
```




