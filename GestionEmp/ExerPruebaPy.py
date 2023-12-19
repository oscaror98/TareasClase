# positivos = 0
# negativos = 0

# for x in range(10):
#     numero = float(input("Ingrese un número: "))
    
#     if numero > 0:
#         positivos += 1
#         print(f"Positivo! y ya van.. {positivos} positivos\n")
#     elif numero < 0:
#         negativos += 1
#         print(f"Negativo! y ya van {negativos} negativos\n")
#     else :
#         print("Número no válido")

# print("\nResultados:")
# print(f"Números positivos: {positivos}")
# print(f"Números negativos: {negativos}")
def dibujar_p(n):
    if n < 3:
        print("El tamaño debe ser igual o mayor a 3.")
        return
    
    # Parte superior (cuadrado)
    print("p" * n)
    
    if(n == 3) :
        # Parte vertical
        for x in range(n-2):
            print("p"+ " " + "p")
    elif()        
    
    # Parte inferior (línea horizontal)
    print("p" * n)

    for x in range(n):
        print("p")
    
n = int(input("Ingrese el tamaño (n >= 3) de la 'p': "))
dibujar_p(n)

