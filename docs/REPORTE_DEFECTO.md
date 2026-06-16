# Reporte de Defecto - LAB10-001

## ID y Título
LAB10-001: aplicar_descuento() permite total negativo al combinar precio rebajado con cupón > 50%

## Pasos para reproducir
1. Importar las funciones `agregar_al_carrito`, `calcular_total` y `aplicar_descuento` del módulo `src.carrito`.
2. Inicializar un carrito de compras vacío.
3. Agregar un producto que ya cuenta con un precio rebajado (ej. Audífonos, precio: 1990, cantidad: 1).
4. Calcular el total del carrito (Total = 1990).
5. Aplicar un descuento del 60% sobre el total calculado usando la función `aplicar_descuento(total, 60)`.

## Resultado esperado
La función no debe retornar un valor menor a 0. Debería existir una validación que impida totales negativos, retornando 0 o levantando una excepción de regla de negocio.

## Resultado obtenido
La función permite el cálculo y retorna un total negativo de -796.0.

## Severidad y Prioridad
Severidad: Alta - Justificación: Un total negativo en un e-commerce rompe la pasarela de pagos y la lógica financiera del negocio, pero no hace colapsar el servidor (por eso Alta y no Crítica).
Prioridad: Alta - Justificación: Impacta directamente los ingresos y el flujo principal de compras, debe solucionarse de inmediato en el sprint actual.

## Entorno
Python: 3.13, pytest: 8.x (última versión instalada), SO: Windows

## Evidencia
Salida por consola al ejecutar el escenario:
```text
-796.0
VALOR NEGATIVO




## Análisis de Causa Raíz (RCA)
1. **¿Qué condición no está siendo validada en aplicar_descuento()?**
No se está validando si el cálculo matemático final del total con descuento produce un valor negativo antes de ejecutar la sentencia `return`.

2. **¿Por qué el porcentaje > 100 ya está validado pero no es suficiente para el escenario del defecto?**
Porque la validación actual solo asegura que un cupón individual no exceda el 100% del valor, pero no contempla el escenario donde la combinación de rebajas previas y cupones apilables genere un saldo negativo o un error de cálculo en la lógica de negocio.

3. **¿Qué cambio mínimo en la función resolvería el defecto sin alterar el comportamiento de los tests existentes?**
Calcular primero el valor del descuento y luego utilizar la función `max(0.0, resultado)` en el retorno, asegurando así que el valor más bajo posible que la función pueda devolver sea siempre `0.0`.