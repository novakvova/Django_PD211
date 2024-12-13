message = lambda: print("Привіт козак :)")
message()

add = lambda a,b: print(f"a+b={a+b}")
add(2,4)

#Перетворення типів int(), float(), str()
a=35
print(str(a))

result = 12
def summa(a, b):
    #global result
    result = a+b
    print(f"result = {result}")

summa(23,45)

print(f"result = {result}")