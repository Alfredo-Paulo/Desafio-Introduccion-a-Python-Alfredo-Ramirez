def calcular_utilidades(precio_suscripcion_normal, precio_suscripcion_premium, num_usuarios_normal, num_usuarios_premium, gastos_totales):
    utilidades = (precio_suscripcion_normal * num_usuarios_normal + precio_suscripcion_premium * num_usuarios_premium) - gastos_totales
    return utilidades

def main():
    print("Este programa calcula las utilidades del proyecto considerando usuarios normales y premium.")
    precio_suscripcion_normal = float(input("Ingrese el precio de suscripción para usuarios normales: "))
    precio_suscripcion_premium = 1.5 * precio_suscripcion_normal  
    num_usuarios_normal = int(input("Ingrese el número de usuarios normales: "))
    num_usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
    gastos_totales = float(input("Ingrese los gastos totales: "))

    utilidades = calcular_utilidades(precio_suscripcion_normal, precio_suscripcion_premium, num_usuarios_normal, num_usuarios_premium, gastos_totales)
    print(f"Las utilidades del proyecto son: {utilidades}")

if __name__ == "__main__":
    main()