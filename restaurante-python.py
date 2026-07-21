# ==========================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# FUNDAMENTOS DE PROGRAMACIÓN
# FASE 5 - EVALUACIÓN FINAL POA
#
# Autor: Miguel Antonio Castillo Castillo
#
# Sistema de gestión de promociones para restaurante
# ==========================================================

# MATRIZ
menu = [
    ["Hamburguesa Artesanal", "Comida Rapida", 18000],
    ["Pizza Familiar", "Comida Italiana", 22000],
    ["Perro Especial", "Comida Rapida", 17000],
    ["Tacos Mexicanos", "Comida Mexicana", 15000],
    ["Ensalada Campesina", "Comida Saludable", 14000],
    ["Sopa Casera", "Comida Saludable", 12000],
    ["Sandwich de Pollo", "Comida Rapida", 16000],
    ["Postre Tres Leches", "Postres", 10000]
]


# FUNCIÓN
def calcular_precio_final(precio_base, categoria):

    categoria_objetivo = "Comida Rapida"
    umbral_precio = 15000

    if categoria == categoria_objetivo and precio_base > umbral_precio:
        return precio_base * 0.85

    return precio_base


# ENCABEZADO
def mostrar_bienvenida():

    print("=" * 70)
    print("        RESTAURANTE SABORES DEL TOLIMA")
    print("=" * 70)

    print("Bienvenido.")
    print()
    print("Este sistema permite consultar el menú,")
    print("seleccionar productos y aplicar promociones")
    print("según las condiciones establecidas.")
    print()

    print("PROMOCIÓN ESPECIAL:")
    print("15% de descuento en productos de")
    print("'Comida Rapida' cuyo precio sea")
    print("superior a $15.000.")
    print("=" * 70)


# MENÚ DE PRODUCTOS
def mostrar_menu():

    print("\nMENÚ DISPONIBLE")
    print("-" * 70)

    for i in range(len(menu)):

        nombre = menu[i][0]
        categoria = menu[i][1]
        precio = menu[i][2]

        print(f"{i+1}. {nombre}")
        print(f"   Categoría: {categoria}")
        print(f"   Precio Base: ${precio:,.0f}")
        print()

    print("0. Finalizar pedido")


# FACTURA
def mostrar_factura(pedido):

    print("\n")
    print("=" * 70)
    print("                 FACTURA DEL CLIENTE")
    print("=" * 70)

    total = 0

    if len(pedido) == 0:
        print("No se registraron productos.")
        return

    for producto in pedido:

        nombre = producto[0]
        precio_base = producto[1]
        precio_final = producto[2]

        print(f"Producto      : {nombre}")
        print(f"Precio Base   : ${precio_base:,.0f}")
        print(f"Precio Final  : ${precio_final:,.0f}")
        print("-" * 70)

        total += precio_final

    print(f"TOTAL A PAGAR: ${total:,.0f}")
    print("=" * 70)
    print("Gracias por su visita.")
    print("¡Esperamos verlo nuevamente!")
    print("=" * 70)


# PROGRAMA PRINCIPAL
def iniciar_sistema():

    pedido = []

    mostrar_bienvenida()

    while True:

        mostrar_menu()

        try:

            opcion = int(input("\nSeleccione un producto: "))

            if opcion == 0:
                break

            if 1 <= opcion <= len(menu):

                producto = menu[opcion - 1]

                nombre = producto[0]
                categoria = producto[1]
                precio_base = producto[2]

                precio_final = calcular_precio_final(
                    precio_base,
                    categoria
                )

                pedido.append([
                    nombre,
                    precio_base,
                    precio_final
                ])

                print("\n✅ Producto agregado correctamente.")

                if precio_final < precio_base:

                    descuento = precio_base - precio_final

                    print(
                        f"Promoción aplicada. "
                        f"Ahorro: ${descuento:,.0f}"
                    )

                print(
                    f"Valor a pagar por este producto: "
                    f"${precio_final:,.0f}"
                )

            else:
                print("Opción no válida.")

        except ValueError:
            print("Ingrese solamente números.")

    mostrar_factura(pedido)


# EJECUCIÓN
if __name__ == "__main__":
    iniciar_sistema()
