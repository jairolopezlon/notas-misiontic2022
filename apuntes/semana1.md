# Semana 1

## Dia 1 - Manejo de texto y impresion por pantalla

para mostrar texto por pantalla se realiza por medio
del metodo `print()`, este recibe un String como parametro,
al ejecutarse este se muestra por medio de consola

### Sintaxis de un String

se tiene dos caminos que se pueden usar para crear un string, es en
caso que solo queramos imprimir una o algunas veces un string, o en caso
que se tenga algun formato preestablecido, por ejemplo que se solo cambie
una parte del texto pero los demas se mantenga igual, algo como una plantilla

#### _Cuando no se tiene una plantilla_

para este caso se tiene dos opciones, usar comillas simple o comillas dobles,
como ejemplo se tiene:

```python
# comillas simples
'texto de comillas simples'

# comillas dobles
"texto de comillas dobles"
```

#### _Cuando se tiene una plantilla_

para este ejemplo utilizaremos un saludo, el cual sera `hola (persona)`.
se tiene 3 formas de lograr asignar un valor a un texto y usarlo como plantilla;
para todos los casos recibiremos por medio de un input el nombre de la persona,
para luego usarlo en los 3 modos que se tienen.

```python
nombre = input('Cual es tu nombre?')
```

los siguientes ejemplos de imprimir el mesaje daran todos el mismo resultado

```python
# hola (nombre)
```

-   modo 1, para este caso se usara el metodo `format()`
    ```python
    print('Hola {}'.format(nombre)
    ```
-   modo 2, para este caso la variable se puede escribir directamente dentro del texto
    , para ellos se requiere antes del abrir las comillas escribir la letra **f**.

    ```python
    print(f'hola {nombre}')
    ```

-   modo 3, por ultimo se tiene la opcion del modulo `Template`, el cual se debe importar
    antes de usar

    ```python
    from string import Template
    texto = Template('Hola $nombre')
    texto.substitute(nombre = nombre)
    ```

texto generado con base en la informacion encontrada en el siguiente enlace: [**_fuente_**](https://realpython.com/python-string-formatting/)
