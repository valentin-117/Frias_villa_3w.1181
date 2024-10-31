print("")
print("Frias villa angel valentin-1181 3W")
print("")

def mostrar_creditos(asignaturas):# Se define la funcion
    # Inicia el contador de creditos
    total_creditos = 0

    # Mostramos los créditos de cada asignatura
    for asignatura, creditos in asignaturas.items():
        print(f"{asignatura} tiene {creditos} créditos")
        total_creditos += creditos

    # Mostramos el número total de créditos del curso
    print(f"El total de créditos del curso es: {total_creditos}")

def main():
    # Diccionario con las asignaturas y sus créditos
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    mostrar_creditos(asignaturas)
# funcion principal del programa
if __name__ == "__main__":
    main()
