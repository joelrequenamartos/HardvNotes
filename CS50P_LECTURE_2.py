#While loop
i = 3
while i != 0:
    print("meow")
    i = i - 1
    
f = 0
while f + 1 <= 3: #we could change <= to < // or count up to 2
    print("woof")
    f += 1 #f++ does not work, sad.
    
#for loop
# This iterates in between a list of items
for i in [0, 1, 2]:
    print("meow?")

for _ in range(3):
    print("Guau")
    
print("Meow " * 3)
print("Meow\n" * 3, end="")

while True:
    n = int(input("What does N equals to? "))
    if n < 0:
        continue
    else:
        break
    
for _ in range(n):
    print("Meow")
    
def main():
    number = getNumber()
    meow(number)
    
def getNumber():
    while True:
        n = int(input("Type a positive number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("MEOWW")

main()

#list
students = ["Hermione", "Harry", "Ron"]
"""

print(students[0])
print(students[1])
print(students[2])
print("-------1")

for students in students:
    print (students)
print("-------2")

"""

#Le pedimos que de largo de students "len(students)"
# nos saque un rango para hacer un bucle en el que
# i vaya recorriendo todos los posibles valores de la lista

for i in range(len(students)):
    print(i + 1, students[i])
print("-------")

#diccionarios dict
"""
students2 = ["Hermione", "Harry", "Draco"]
houses = ["Gryff", "Griff", "Slyth"]
"""

estudiantes = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Draco":"Slytherin"
}

for printNombres in estudiantes:
    print(printNombres, estudiantes[printNombres], sep=", from ")
