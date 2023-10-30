#Conditionals
x = int(input("What's x? "))
y = int(input("What's y? "))

#if 

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")
    
if x == y:
    print("x is equal to y")


#elif and else

x1 = int(input("What's x? "))
y1 = int(input("What's y? "))

if x1 < y1:
    print("x is less than y")
elif x1 > y1:
    print("x is greater than y")
else:
    print("x is equal to y")
    
if (x1 > y1) or (x1 < y1):
    print("Those numbers are not equal")
else:
    print("Those numbers are equal")

if x1 != y1:
    print("Those numbers are not equal")
else:
    print("Those numbers are equal")
    
score =  int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
else:
    print("Grade F")
    

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
    
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("other notes")