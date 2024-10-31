print("")
print("Frias villa angel valentin-1181 3W")
print("")

def main():
    # Declara lalista de asignaturas
    asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    notas = []

    # Se pide al usuario la nota de cada asignatura
    for asignatura in asignaturas:
        nota = input(f"Introduce la nota en {asignatura}: ")
        notas.append(nota)

    # Se imprimen las notas en pantalla
    for asignatura, nota in zip(asignaturas, notas):
        print(f"En {asignatura} has sacado {nota}")

if __name__ == "__main__":
    main()
