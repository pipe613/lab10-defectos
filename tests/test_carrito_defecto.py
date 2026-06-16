import pytest
from src.carrito import aplicar_descuento

@pytest.mark.parametrize('total, porcentaje, esperado_minimo', [
    # (total original, % descuento, valor mínimo aceptable)
    (1990, 60, 0),  # rebajado 50% + cupón 60% -> negativo sin corrección
    (500, 80, 0),   # caso límite
    (1000, 100, 0), # descuento total
    (2000, 50, 0)   # 50% exacto -> frontera
])
def test_descuento_no_genera_total_negativo(total, porcentaje, esperado_minimo):
    # Arrange
    # (parámetros ya definidos arriba)

    # Act
    resultado = aplicar_descuento(total, porcentaje)

    # Assert
    assert resultado >= esperado_minimo, (
        f"Total con descuento {porcentaje}% sobre {total} fue {resultado}, "
        f"se esperaba >= {esperado_minimo}"
    )