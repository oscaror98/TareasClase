# Crear una lista de listas con medida y peso
lista_datos = [
   [1.75, 68],
   [1.60, 55],
   [1.80, 75],
   [1.65, 60],
]


# Imprimir la lista de datos
print("Lista de datos:")
for datos in lista_datos:
   print(f"Medida: {datos[0]} m, Peso: {datos[1]} kg")

# Ordenar la lista por mayor altura y, en caso de igualdad, por menor peso
# key function -> Usadas para proporcionar una función que devuelve un valor clave y con este ordenar elementos en lista


lista_ordenada = sorted(lista_datos, key=lambda x: (x[0], -x[1]))


# Imprimir la lista ordenada
print("Lista ordenada:")
for datos in lista_ordenada:
   print(f"Medida: {datos[0]} m, Peso: {datos[1]} kg")
   

