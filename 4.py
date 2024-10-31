
print("")
print("Frias villa angel valentin-1181 3W")
print("")
def main():
    # Crear un diccionario para almacenar la información del usuario
    usuario = {}

    # Pide al usuario ingresar sus datos
    usuario['nombre'] = input("Introduce tu nombre: ")
    usuario['edad'] = input("Introduce tu edad: ")
    usuario['dirección'] = input("Introduce tu dirección: ")
    usuario['teléfono'] = input("Introduce tu número de teléfono: ")

    # muestra la informacion en orden
    print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['dirección']} y su número de teléfono es {usuario['teléfono']}.")

if __name__ == "__main__":
    main()
