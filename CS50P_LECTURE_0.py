print("hello, world")
#function("argument")

#input("yoo wasup man ")
#We are asking a user for its name
name = input("What's your name? ")

#Print the results
print(name)
print("Hello " + name)
print("Hello,", name)

'''
This is a multiline
comment section
'''

#print Parameters
print("Hello, ", end="")
print(name)

print("hello", name, sep="x")

# Print Quote
print("hello, \"friend\"")
print('hello, "friend"')

#Format Strings
print(f"hello, {name}")

#Clean Strings
    #Remove whitespaces from str
name2 = (input("What's your name again? "))
name2 = name2.strip()
print(name2)

    #Capitalize the first word
name2 = name2.capitalize()
print(name2)

    #Capitalize all
name2 = name2.title()
print(name2)

    #You can do both at the same time
name3 = (input("What's your name again? ")).strip().title()
print(name3)

    #You can add as many .title().strip()... etcetc


    #Split user's name into first and last name
first, last = name3.split(" ")
print(first)
print(last)

#Functions
def hello(to="World"):
    print("hello, ", to)


namefun = input("What is your name? ")
hello(namefun)
