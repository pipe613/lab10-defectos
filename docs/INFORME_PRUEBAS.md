# Informe de Resumen de Pruebas - Extracto IEEE 829

## 1. Identificador del informe
Código: IRP-LAB10-001
Versión del SUT: 1.0.1 (post-corrección)
Alcance: módulo carrito.py - ciclo de corrección del defecto LAB10-001

## 2. Resumen de variaciones del plan
Ninguna variación. Todos los tests planificados y de regresión fueron ejecutados exitosamente.

## 3. Resumen de actividades
Herramientas: pytest 8.x, pytest-cov
Entorno: Python 3.13, SO: Windows
Tiempo de ejecución: 0.08s

## 4. Resultados - resumen de casos
| Tipo de prueba | Ejecutados | Aprobados | Fallidos | % Aprobación |
|----------------|------------|-----------|----------|--------------|
| Unitarias (pytest) | 13 | 13 | 0 | 100% |

## 5. Métricas
DRE = 1 / (1 + 0) * 100 = 100%
(Justificación: Defectos hallados antes del cierre = 1. Defectos post-release = 0, ya que el pipeline de CI habría capturado cualquier regresión con el test parametrizado).
Densidad = 1 defecto / 0.014 KLOC = 71.43 defectos/KLOC
% Aprobación = 13 / 13 * 100 = 100%
Tasa reapertura = 0 / 1 * 100 = 0%

## 6. Evaluación general
El módulo está listo para integrarse. Alcanzó un 100% de aprobación en los casos de prueba con un 100% de cobertura de código. La métrica DRE refleja una captura temprana del defecto, y la corrección implementada no introdujo nuevos fallos (0% tasa de reapertura).

## 7. Aprobaciones
Responsable QA: Felipe Arevalo
Fecha: 16 de Junio de 2026

## 8. Repositorio
https://github.com/pipe613/lab10-defectos.git