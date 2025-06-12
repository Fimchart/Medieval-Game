from funGame import personajes
import time


print("\n-----  BIENVENID@  -----\n")
continua = True

print("...........................\n")
time.sleep(1)
print("En un mundo medieval, donde la caza de brujas es persistente y los pueblos luchan por comida.\n")
time.sleep(1)
print("Eres un.....\n")
time.sleep(1)

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
        time.sleep(1)
        print("Tu antecesor fue asesinado en una guerra por el pueblo enemigo.")
        time.sleep(1)
        nombre = input("Tu nombre es ..... ")

        print(f"Tu pueblo solo ha escuchado tu nombre.")
        print(nombre)
        time.sleep(1)
        print("Cuando fuiste elegido, fuertes rumores circularon.")
        time.sleep(1)
        print("Muchos piensan que eres un ogro, quien tomó el puesto por la fuerza.")
        time.sleep(1)
        print("Otros, que eres un niño al quien le cumplieron su capricho de reinar.")
        time.sleep(1)
        print("Pensaste que era absurdo.")
        time.sleep(1)
        print("Tienes certeza de que no eres un ogro.")
        time.sleep(1)

        edad = int(input("Tampoco eres un niño, tienes .... "))

    elif personaje == 2:
        print("Eres un principe!")
    elif personaje == 3:
        print
    elif personaje == 4:
        print
    elif personaje == 5:
        break