def calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales):
    utilidades = precio_suscripcion * num_usuarios - gastos_totales
    return utilidades

def main():
    print("Este programa calcula las utilidades del proyecto.")
    precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
    num_usuarios = int(input("Ingrese el número de usuarios: "))
    gastos_totales = float(input("Ingrese los gastos totales: "))
    utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

    utilidades_actuales = calcular_utilidades(precio_suscripcion, num_usuarios, gastos_totales)
    print(f"Las utilidades del proyecto son: {utilidades_actuales}")

    if utilidades_anterior != 0:
        razon_utilidades = utilidades_actuales / utilidades_anterior
        print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")
    else:
        print("No se puede calcular la razón porque las utilidades del año anterior son cero.")

if __name__ == "__main__":
    main()