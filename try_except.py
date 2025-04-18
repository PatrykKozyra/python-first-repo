# a = 4
# b = 5

# try:
#     result = a/b
    
#     if a == 4:
#         raise Exception()
    
# except ZeroDivisionError as err:
#     print("Nie mozna dzielic przez 0")
# except TypeError as err:
#     print("Liczby musza byc poprawne")
# except Exception as err:
#     print("Nieznany blad")


# is_digit = "123".isdigit()
# is_alpha = "abc".isalpha()

# if is_digit:
#     print("Masz racje, to liczby")
    
# if is_alpha:
#     print("Masz racje, to litery")
    
    
    
# input_ocena = str(input("Podaj ocene w skali 1-6: "))

# match input_ocena:
#     case "1":
#         ocena = "Niedostateczny"
#     case "2":
#         ocena = "Dopuszczajacy"
#     case "3":
#         ocena = "Dostateczny"
#     case "4":
#         ocena = "Dobry"
#     case "5":
#         ocena = "Bardzo Dobry"
#     case "6":
#         ocena = "Celujacy"
    
# print(f"Twoja ocena to {ocena}")


##########################################################

# Pobieranie nazwy użytkownika
user_input = input("Podaj nazwę użytkownika: ")

try:
    cleaned_input = user_input.replace(" ", "")

    if len(cleaned_input) < 5:
        raise Exception("Nazwa użytkownika powinna mieć co najmniej 5 znaków.")

    if not cleaned_input.isalpha():
        raise Exception("Tylko litery są dozwolone.")

    # Jeśli wszystkie warunki są spełnione
    print("Nazwa użytkownika jest poprawna!")

except Exception as err:
    print(f"Błąd: {err}")