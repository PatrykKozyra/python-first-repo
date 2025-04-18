# is_true = True
# is_false = False

#print(12>12)
# is_valid = 14 > 10
# print(is_valid)

# num = 7

# if num > 5:
#     print("Masz racje")
#     print("Liczba jest wieksza")
    
# else:
#     print("warunek nie zostal spelniony")


# account = "admin"

# if account == "admin":
#     print("witamy admina")
# elif account == "mod":
#     print("witaj moderatorze")
# elif account == "user":
#     print("zwykly uzytkownik")
# else:
#     print("nie rozpoznano")

# account = "admin"
# is_auth = False
# test = 5

# if account == "admin" and is_auth == True and test == 5:
#     print("witamy w panelu")
# else:
#     print("odmowa dostepu")
    

# on_sale = True
# code = "2025"
# price = 199

# if on_sale == True or code == "2025":
#     price = price * 0.8
#     print(f"Cena promocyjna {price}")
# else:
#     print("standardowa cena")
    
    
    
###############################################################    
# # 1.
# # Napisz dwie zmienne o nazwie user_role i is_logged
# # Następnie przygotuj instrukcję warunkową która sprawdza typ konta zalogowanego użytkownika:

# user_role = "admin"
# is_logged = True

# -Jeśli użytkownik jest zalogowany i jest administratorem wyświetlaj napis "Witaj w panelu admina"
# -Jeśli użytkownik jest moderatorem i jest zalogowany wyświetlaj napis "Witaj w panelu moderatora"
# -Jeśli uzytkownik loguje się na zwykłe konto i jest zalogowany wyświetlaj napis "Witaj w panelu użytkownika"
# -W każdym innym przypadku wyświetlaj napis błąd logowania

# if is_logged == True and user_role == "admin":
#     print("Witaj w panelu admina")
# elif user_role == "mod" and is_logged == True:
#     print("Witaj w panelu moderatora")
# elif user_role == "user" and is_logged == True:
#     print("Witaj w panelu użytkownika")
# else:
#     print("blad logowania")




###############################################################
# 2.
# Prowadzisz sklep, który dostarcza towar jedynie do Polski, Niemiec i Czech

# Napisz zmienną o nazwie user_country
# Następnie zaprojektuj instrukcję warunkową która sprawdzi czy kupujący składa zamówienie z któregoś z powyższych krajów, 
# jeśli NIE, wyświetlaj tekst: Dostawa towaru niemożliwa

# list_of_countries = ["Polska", "Niemcy", "Czechy"]
# user_country = input("Podaj kraj zamowienia:")

# if user_country not in list_of_countries:
#     print("Dostawa towaru niemożliwa")
# else:
#     print(f"Dostawa towaru do {user_country} jest mozliwa")



###############################################################
# 3.
# Spróbuj napisać zmienną, w której za pomocą Pythona umieścisz informacje o aktualnej godzinie

# Następnie napisz instrukcję warunkową, która wyświetla powitanie w zależności od pory dnia
# -Między 6 a 12 "Good Morning"
# -Między 12 a 18 "Good Afternoon"
# -Powyżej 18 "Good Evening"

# from datetime import datetime
# current_time = datetime.now().hour

# if 6 <= current_time < 12:
#     print("Good Morning")
# elif 12 <= current_time < 18:
#     print("Good Afternoon")
# elif current_time >= 18:
#     print("Good Evening")
# else:
#     print("Error, value out of scope")
# print(current_time)

###############################################################
# 4. Napisz program, który sprawdza, czy podany przez użytkownika kod PIN jest poprawny. PIN:
# - Musi składać się z dokładnie 6 cyfr.
# - Nie może zawierać liter
# Kod pin podawaj w inpucie

# pin = "123444"
# allowed_len_of_pin = 6

# pin_input = input("Podaj PIN: ")


# def has_three_consecutive_digits(ppin_inputin):
#     for i in range(len(pin_input) - 2):
#         if pin_input[i] == pin_input[i + 1] == pin_input[i + 2]:
#             return True
#     return False


# if (
#     len(pin_input) == allowed_len_of_pin
#     and pin_input == pin
#     and pin_input.isdigit()
#     and not has_three_consecutive_digits(pin_input)
# ):
#     print("Kod PIN jest poprawny")
# else:
#     print("Kod PIN niepoprawny")


# if len(pin_input) == allowed_len_of_pin and pin_input == pin and pin_input.isdigit():
#     print("Kod PIN jest poprawny")
# else:
#     print("Kod PIN niepoprawny")
    
########################################################################################

# truly values:
# True, 1 i inne liczby, "string", [...]

# falsely values
# False, 0, "", None, [] pusta lista, {} 

# email = input("Podaj email: ")
# if email:
#     print("dziala")


# switch -> match
#instrukcja match

# user_country = "Finlandia"
# price = 100

# match user_country:
#     case "Polska" | "Finlandia":
#         price *= 1.23
#     case "Francja":
#         price *= 1.18
#     case "Niemcy":
#         price *= 1.20
        
        
# print(f"Do zaplaty {price}")




