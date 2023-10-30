name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griff")
    case "Draco":
        print("Slyth")
    case _:
        print("Who?")