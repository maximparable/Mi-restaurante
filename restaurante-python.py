# ==========================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# FUNDAMENTOS DE PROGRAMACIÓN
# FASE 5 - EVALUACIÓN FINAL POA
#
# Autor: Miguel Antonio Castillo Castillo
#
# Problema 2:
# Gestión de precios de un menú de restaurante aplicando
# promociones según categoría y precio base.
# ==========================================================


def mostrar_encabezado():
    print("=" * 75)
    print("      RESTAURANTE SABORES DEL TOLIMA")
    print("=" * 75)
    print("Bienvenido al sistema de análisis de promociones gastronómicas.")
    print()
    print("Este programa permite consultar un menú de productos y calcular")
    print("automáticamente descuentos especiales para determinados platos.")
    print()
    print("La promoción consiste en aplicar un descuento del 15% a los")
    print("productos que pertenezcan a una categoría específica y cuyo")
    print("precio base supere un valor mínimo establecido.")
    print()
    print("Desarrollado como evidencia académica para la asignatura")
    print("Fundamentos de Programación.")
    print("=" * 75)
    print()


def calcular_precio_final(precio_base, categoria):
    """
    Calcula el precio final de un producto aplicando
    una promoción específica.
    """

    categoria_objetivo = "Comida Rapida"
    umbral_precio = 15000

    if categoria == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


def mostrar_menu(menu):
    print("\nLISTADO GENERAL DE PRODUCTOS")
    print("-" * 75)

    for producto in menu:

        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        precio_final = calcular_precio_final(
            precio_base,
            categoria
        )

        print(f"Producto      : {nombre}")
        print(f"Categoría     : {categoria}")
        print(f"Precio Base   : ${precio_base:,.0f}")
        print(f"Precio Final  : ${precio_final:,.0f}")

        if precio_final < precio_base:
            ahorro = precio_base - precio_final
            print(f"Descuento     : ${ahorro:,.0f}")
            print("Promoción     : Aplicada ✅")
        else:
            print("Promoción     : No aplica")

        print("-" * 75)


def mostrar_resumen(menu):

    total_base = 0
    total_final = 0

    for producto in menu:

        precio_base = producto[2]

        precio_final = calcular_precio_final(
            precio_base,
            producto[1]
        )

        total_base += precio_base
        total_final += precio_final

    ahorro_total = total_base - total_final

    print("\nRESUMEN GENERAL")
    print("=" * 75)
    print(f"Valor total sin descuentos : ${total_base:,.0f}")
    print(f"Valor total con descuentos : ${total_final:,.0f}")
    print(f"Ahorro generado            : ${ahorro_total:,.0f}")
    print("=" * 75)


# ---------------- MATRIZ DE PRODUCTOS ----------------

menu_restaurante = [

    ["Hamburguesa Artesanal", "Comida Rapida", 18000],
    ["Pizza Familiar", "Comida Italiana", 22000],
    ["Perro Especial", "Comida Rapida", 17000],
    ["Tacos Mexicanos", "Comida Mexicana", 15000],
    ["Ensalada Campesina", "Comida Saludable", 14000],
    ["Sopa Casera", "Comida Saludable", 12000],
    ["Sandwich de Pollo", "Comida Rapida", 16000],
    ["Postre Tres Leches", "Postres", 10000]

]

# ---------------- PROGRAMA PRINCIPAL ----------------

mostrar_encabezado()
mostrar_menu(menu_restaurante)
mostrar_resumen(menu_restaurante)

print()
print("Gracias por utilizar el sistema.")
print("Que tenga un excelente día.")
