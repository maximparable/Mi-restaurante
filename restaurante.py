# SISTEMA DE PEDIDOS PARA RESTAURANTE
platillos = ["Hamburguesas", "Pizzas", "Sanduches", "Perros Calientes", "Tacos", "Ensaladas", "Sopas", "Postres"]
precios = [18000, 21000, 12000, 9000, 15000, 16000, 6000, 8000]
pedido_cliente = []
precios_cliente = []

def mostrar_menu():
    print("----- MENÚ DEL RESTAURANTE -----")
    for i in range(len(platillos)):
        print(f"{i + 1}. {platillos[i]} - ${precios[i]:,.0f})")
    print("---------------------------------")
    print("Seleccione un platillo por su número")

def agregar_al_pedido(opcion):
    indice = opcion - 1
    pedido_cliente.append(platillos[indice])
    precios_cliente.append(precios[indice])
    print(f"\n--> Agregaste: {platillos[indice]} (${precios[indice]: ,.0f})")

def generar_factura():
    print("\n" + "*"*40 + "\n       FACTURA DE PEDIDO     \n" + "*"*40)
    if len(pedido_cliente) == 0:
        print("No se han agregado ningun platillo.")
    else:
        for i in range(len(pedido_cliente)):
             print(f"- {pedido_cliente[i]}: ${precios_cliente[i]:,.0f}")
        print("-" * 40 + f"\nTOTAL A PAGAR: ${sum(precios_cliente):,.0f}")
        print("*" *40 + "\n¡Gracias por su compra, Vuelva pronto!")
    print("-------------------")

def iniciar_sistema():
    print("Entré a iniciar_sistema")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nIngresa el numero de tu opcion: "))
            if opcion == 0:
                generar_factura()
                break
            elif 1 <= opcion <= len(platillos):
                agregar_al_pedido(opcion)
            else:
                print("\n[ERROR] Opcion no valida. Elige un numero del 0 al 8")
        except ValueError:
            print("\n[ERROR] Por favor, ingresa unicamente numeros enteros")  

if __name__ == "__main__":
                iniciar_sistema()