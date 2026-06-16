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