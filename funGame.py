def personajes():
    print("1. Rey")
    print("2. Principe")
    print("3. Guardia real")
    print("4. Campesino\n")


def camino_edad(edad):
    if edad >= 60:
        print("Eres un hombre experimentado.")
        print("Quien ha vivido viendo los errores de los que lo rodean.")
        print("Has recorrido todos lo rincones que has podido encontrar.")
        print("Gracias a esto, fuiste capaz de hallar: El Ojo de Itharel")
    elif edad >= 40:
        print("Eres un hombre en la cuspide de la madurez")
        print("Has cometido errores y aprendido de ellos.")
        print("Tu liderazgo es tu arma.")