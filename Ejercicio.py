while True:
    print("Bienvenido a la veterinaria")
    try:
        cantidad = int(input("Ingrese la cantidad de animales: "))
        break
    except ValueError:
        print("Solo están permitidos los numeros.")

mas_de_5 = 0
menos_o_igual = 0


for i in range(cantidad):
    raza = input("Ingrese la raza de su mascota: ")

    valido = False
    while not valido:
        try:
            años = int(input("Ingrese los años de su mascota: "))
            valido = True
        except ValueError:
            print("Solo numeros.")
    if años > 5:
        print("Le corresponde el conjunto de vacunas de tipo B")
        mas_de_5 =+1
    else: 
        print("Le corresponde el conjunto de vacunas tipo A")
        menos_o_igual =+1


print(f"Se registraron: {mas_de_5} animales con mas de 5 años de vida")
print(f"Se registraron: {menos_o_igual} animales con mas de 5 años de vida")