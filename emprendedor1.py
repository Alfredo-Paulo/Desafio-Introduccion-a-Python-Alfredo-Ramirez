def calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales):
    utilidades = precio_suscripcion * num_usuarios - gastos_totales
    return utilidades

def main():
    print("Este programa calcula las utilidades del proyecto.")
    precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
    num_usuarios = int(input("Ingrese el número de usuarios: "))
    gastos_totales = float(input("Ingrese los gastos totales: "))

    utilidades = calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales)
    print(f"Las utilidades del proyecto son: {utilidades}")

if __name__ == "__main__":
    main()