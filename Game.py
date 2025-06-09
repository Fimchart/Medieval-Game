from funGame import personajes


print("\n-----  BIENVENID@  -----\n")
continua = True

print("...........................\n")
print("En un mundo medieval, donde la caza de brujas es persistente y los pueblos luchan por comida.\n")
print("Eres un.....\n")

personajes()
while continua:
    try:
        personaje = int(input())
        if 1 <= personaje <= 4:
            break
        else:
            print("Por favor, elige un número del 1 al 4.")
    except ValueError:
        print("Solo están permitidos los numeros.")
        continue
    
if personaje == 1:
    print("¡Eres el nuevo rey del pueblo Nayhem!")
    print("Tu antecesor fue asesinado en una guerra por el pueblo enemigo.")
    nombre = input("Tu nombre es ..... ")

    print(f"Tu pueblo solo ha escuchado tu nombre.")
    print(nombre)
    print("Cuando fuiste elegido, fuertes rumores circularon.")
    print("Muchos piensan que eres un ogro, quien tomó el puesto por la fuerza.")
    print("Otros, que eres un niño al quien le cumplieron su capricho de reinar.")
    print("Pensaste que era absurdo.")
    print("Tienes certeza de que no eres un ogro.")

    edad = int(input("Tampoco eres un niño, tienes .... "))

elif personaje == 2:
    print
elif personaje == 3:
    print
elif personaje == 4:
    print