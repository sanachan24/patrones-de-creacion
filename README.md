# Patrones de Creación – Abstract Factory

## Descripción del proyecto

Este proyecto consiste en la implementación del patrón de diseño creacional **Abstract Factory** utilizando el lenguaje de programación Python.

El sistema permite crear y procesar diferentes tipos de informes, organizados en tres categorías: ENTRADA, SALIDA y MIXTA.

## Objetivo

Aplicar el patrón Abstract Factory para organizar la creación de objetos, facilitar el mantenimiento del código y permitir la incorporación de nuevas categorías y tipos de informes.

## Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

- **main.py:** contiene la lista de informes y ejecuta el procesamiento.
- **productos.py:** define los productos abstractos y concretos.
- **fabricas.py:** contiene la fábrica abstracta y las fábricas concretas.
- **procesador.py:** identifica las categorías y los tipos de informes, selecciona la fábrica correspondiente y ejecuta su procesamiento.

## Categorías y tipos de informes

| Categoría | Tipos de informes |
|---|---|
| ENTRADA | FACTURA, COMPRA y PEDIDO |
| SALIDA | FACTURA y COMPRA |
| MIXTA | FACTURA y COMPRA |

## Tecnologías utilizadas

- Python 3.
- Programación orientada a objetos.
- Patrón de diseño Abstract Factory.

## Requisitos

Tener Python 3 instalado en el computador.

## Cómo ejecutar el proyecto

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal dentro de la carpeta.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

## Resultado esperado

Al ejecutar el programa, se procesan siete informes y se muestra en la terminal un mensaje que identifica la categoría y el tipo de cada uno.

## Contexto académico

Proyecto desarrollado como actividad académica de la asignatura Reutilización de Software, correspondiente al tema Patrones de Creación.
