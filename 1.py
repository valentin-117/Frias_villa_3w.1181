print("")
print("Frias villa angel valentin-1181 3W")
print("")

asignaturas=["Matematicas","Ecosistemas", "Fisica", "lengua", "Frameworks"] # Almacena las asignaturas a ingresar

notas= {} #Crea un dicccionario vacio para almacenar las notas (calificaciones)

for asignatura in asignaturas:
    # Requiere ingresar la nota al usuario. 
    nota= float(input("ingresa la nota de "+ asignatura + ":"))
    notas[asignatura] = nota
# Revisa la calificacion ingresada
for asignatura,nota in notas.items():
    if nota >= 5.0:
        asignaturas.remove(asignatura)

# Imprime en pantalla las asignaturas que el usuario recursará
print("Las asignaturas a recursar son: ")
for asignatura in asignaturas:
    print(asignatura)