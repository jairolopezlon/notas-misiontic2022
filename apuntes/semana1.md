# Semana 1

## Contenido

-   [Manejo de texto e impresion por pantalla](#1)
-   [Ingreso de informacion](#2)
-   [Parsear tipo de datos](#3)

## Manejo de texto y impresion por pantalla <span name="1">

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
    resultado = texto.substitute(nombre = nombre)
    print(resultado)
    ```

## Ingreso de informacion <span name="2">

Para ingreso de infomacion, se utiliza el metodo `input()`, este recibe un
parametro opcional, puede ser una cadena de texto, numero o combinacion de ambos.

_parametro:_ `str`, `int`, `float`, o `bool`

_return:_ `str`

Ejemplo de codigo:

```python
nombre = input('Como te llamas?') #por medio de consola ingresamos la respues - "Pedro"

print('Hola',nombre) #imprime en consola "hola Pedro"

```

## Parsear tipo de datos <span name="3">

para cambia un tipo de dato a otro se utiliza unos metodos que sirven para parsear,
en este caso se explica los metodos `int()` y `str()`.

### Parsear numeros enteros

esto se usara en el momento que se tenga el valor de una variable como un numero pero
que esta en tipo texto, es decir no es lo mismo `32` que `"32"`, mientras que el
primero es de tipo numero el segundo es de tipo texto.

Para cambiar de texto a numero se usa el metodo `int()` de la siguiente manera:

```python
num = "32"
print(num) # imprime 32, pero como texto
print(int(num)) # imprime 32, pero como numero
```

la utilidad de este metodo se vera cuando tengamos algun valor numerico como texto
y se quiera realizar alguna operacion matematica, siguiendo el ejemplo anterior, si
se opera multiplicandole 3 al dato de texto y num obtendremos valores distintos

```python
num = "32"
print(num * 3) # imprime 323232, pero como texto
print(int(num) * 3) # imprime 96, pero como numero
```

esto es importante tenerlo en cuenta al momento de recibir valores por medio del metodo
`input()`, ya que este siempre nos devuelve un valor de tipo texto, por lo que si
ingresamos algun dato numerico, este sera de tipo `str` y no `int`

---

> ### _Fuente de informacion_
>
> _texto generado con base en la informacion encontrada en el
> siguiente enlace: [***realpython.com***](https://realpython.com/python-string-formatting/)_
