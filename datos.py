#Funcion para recibir un numero entero, sino se recibe 
def readint( message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("El dato que ingreso no es numerico, intentelo nuevamente.")

def readnote(mensaje):
    while True:
        try:
            numes = float(input(mensaje))
            if numes < 0 or numes > 5:
                raise ValueError
            return numes
        except ValueError:
            print("El valor no esta en el rando de 0 a 5.")

def receivedata(numes, students):
    for i in range(1, numes + 1):
        name = input(f"Ingrese el nombre del estudiante numero {i}: ")
        numes = readnote(f"Ingrese la nota del estudiante {name}: ")
        if numes >= 3:
            aprobado["Id"] = id
            aprobado["Nombre"] = name
            aprobado["Aprobo con"] = numes
        elif numes < 3:
            aprobado["Id"] = id
            reprobado["Nombre"] = name
            reprobado["Reprobo con"] = numes

        idest = readint(f"Ingrese la identificacion del estudiante {name}: ")
        while idest in students:
            print(f"{idest} ya existe, intentelo nuevamente.")
            idest = readint(f"Ingrese la identificacion del estudiante numero {name}: ")
        students.append(idest)
        promedio.append(numes)

def showstudents(students):
    print(f"Los estudiantes son: {students}")
    print(aprobado, reprobado)
    print(f"El promedio de {numes} estudiates es {sum(promedio)/numes} ")

if __name__ == "__main__":
    id = []
    aprobado = {}
    reprobado = {}
    students = []
    promedio = []
    while True:
        numes = readint("Cuantos estudiantes quiere validar?: ")
        if numes > 0:
            break
        print("El numero no puede ser menor a 0, intentelo nuievamente.")
    receivedata(numes, students)
    showstudents(students)