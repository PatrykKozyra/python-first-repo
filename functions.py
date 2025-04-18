# def fn():
#     print("Test")
    
# fn()


# def add(a,b):
#     return a + b

# result1 = add(2,3)
# result2 = add(9,9)

# print(result1)
# print(result2)



# def multiply(x,y,z):
#     return x * y * z

# multi1 = multiply(4,5,6)
# multi2 = multiply(7,8,9)

# print(multi1)
# print(multi2)


# def checkPassword(password):
#     if len(password) < 6:
#         return False
#     else:
#         return True
    
# password_value = input("Podaj swoje haslo: ")

# result = checkPassword(password_value)

# if result != True:
#     print("Twoje haslo jest niewystarczajaco silne")

value = input("Podaj liczbę: ")

def multiply(num):
    if not num.isdigit():
        print("Wartość nie jest liczbą")
        return
    integer = int(num)
    return integer * 10

result = multiply(value)
print(result) 