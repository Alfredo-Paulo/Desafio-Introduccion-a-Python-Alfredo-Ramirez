import math

def calcular_velocidad_escape(r, g):
    velocidad_escape = math.sqrt(2 * g * r)
    return velocidad_escape

def main():
    print("Este programa calcula la velocidad de escape.")
    print("Por favor, ingrese los siguientes datos:")
    
    radio_km = float(input("Ingrese el radio del planeta en Kilómetros: "))
    constante_g = float(input("Ingrese la constante gravitacional en m/s^2: "))
    
    radio_m = radio_km * 1000
    
    velocidad_escape = calcular_velocidad_escape(radio_m, constante_g)
    
    print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]")

if __name__ == "__main__":
    g = 9.8  
    r = 6371 * 1000  
    
    main()