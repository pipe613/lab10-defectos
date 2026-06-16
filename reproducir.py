# Escenario de reproducción manual
from src.carrito import agregar_al_carrito, calcular_total, aplicar_descuento

carrito = []
# Producto con precio ya rebajado: $1.990 (precio original $3.980 con 50% off)
agregar_al_carrito(carrito, {'nombre': 'Audífonos', 'precio': 1990, 'cantidad': 1})

total = calcular_total(carrito)   # → 1990
total_con_cupon = aplicar_descuento(total, 60)  # 60% sobre $1990
print(total_con_cupon)   # → -796.0 ← VALOR NEGATIVO