# 1. Liczba parzysta czy nieparzysta?
# Napisz program, który pobiera liczbę od użytkownika i sprawdza, czy jest parzysta, czy nieparzysta.
# user_input = input("Podaj liczbe: ")


# if int(user_input) % 2 == 0:
#     print("Liczba jest parzysta.")
# else:
#     print("Liczba jest nieparzysta.")


# 2. Czy jesteś pełnoletni?
# Pobierz wiek użytkownika i sprawdź, czy ma co najmniej 18 lat. Jeśli tak, wypisz „Jesteś pełnoletni!”, w przeciwnym razie „Nie masz jeszcze 18 lat!”.

# users_age = input("Podaj swoj wiek: ")

# if int(users_age) < 18:
#     print("Nie masz jeszcze 18 lat!")
# else:
#     print("Jestes pelnoletni!")

# 3. Największa z dwóch liczb
# Pobierz dwie liczby i wypisz większą z nich. Jeśli są równe, wypisz „Liczby są równe”.

# first_number = input("Podaj pierwsza liczbe: ")
# second_number = input("Podaj druga liczbe: ")

# if int(first_number) == int(second_number):
#     print("Liczby sa rowne")
# elif int(first_number) < int(second_number):
#     print("Druga liczba jest wieksza od pierwszej")
# else:
#     print("Pierwsza liczba jest wieksza od drugiej")

# 4. Kalkulator ocen
# Pobierz ocenę (0-100) i wypisz odpowiadającą jej ocenę szkolną: - 90-100: „A” - 80-89: „B” - 70-79: „C” - 60-69: „D” - poniżej 60: „F”

# grade_input = input("Pobierz ocene 0-100: ")

# match int(grade_input):
#     case grade_input if grade_input < 60:
#         print('F')
#     case grade_input if grade_input < 70:
#         print('D')
#     case grade_input if grade_input < 80:
#         print('C')
#     case grade_input if grade_input < 90:
#         print('B')
#     case grade_input if grade_input >= 90:
#         print('A')

# 5. Czy liczba jest podzielna przez 3 i 5?
# Pobierz liczbę i sprawdź, czy jest podzielna zarówno przez 3, jak i przez 5.

# user_input = input("Podaj liczbe: ")

# if int(user_input) % 3 == 0 and int(user_input) % 5 == 0:
#     print("Liczba jest podzielna przez 3 i 5")
# else:
#     print("Liczba NIE jest podzielna przez 3 i 5")

# 6. Długość hasła
# Pobierz hasło i sprawdź, czy ma co najmniej 8 znaków. Jeśli tak, wypisz „Hasło jest wystarczająco długie”, w przeciwnym razie „Hasło jest za krótkie”.

# password = input("Podaj haslo: ")
# len_of_password = len(str(password))

# if len_of_password < 8:
#     print("Haslo jest za krotkie")
# else:
#     print("Haslo jest wystarczajaco dlugie")

# 7. Czy to samogłoska?
# Pobierz pojedynczy znak i sprawdź, czy jest samogłoską (a, e, i, o, u).

# user_input = input("Podaj jedna litere: ")

# if user_input in ["a","e","i","o","u"]:
#     print("Litera jest samogloska")
# else:
#     print("To nie jest samogloska")

# 8. Kalkulator podatku
# Pobierz zarobki i oblicz podatek: - do 5000 zł – 0% - 5001-10 000 zł – 10% - powyżej 10 000 zł – 20%

# salary = input("Podaj swoje zarobki: ")

# match int(salary):
#     case salary if salary <= 5000:
#         podatek = "0%"
#     case salary if salary <= 10000:
#         podatek = "10%"
#     case salary if salary > 10000:
#         podatek = "20%"

# print(f"Podatek dla kwoty {salary} wynosi {podatek}")

# 9. Czy rok jest przestępny?
# Pobierz rok i sprawdź, czy jest przestępny (podzielny przez 4, ale nie przez 100, chyba że podzielny przez 400).

# year = int(input("Podaj rok: "))

# if year % 400 == 0:
#     print("Rok przestepny")
# elif year % 4 == 0 and not year % 100 == 0:
#     print("Rok przestepny")
# else:
#     print("Rok NIE jest przestepny")

# 10. Temperatura i stan skupienia wody
# Pobierz temperaturę i sprawdź, czy woda jest w stanie stałym (<=0°C), ciekłym (1-99°C) czy gazowym (>=100°C).

# temp = int(input("Podaj temperature: "))

# if temp <= 0:
#     print("Woda jest w stanie stalym")
# elif temp <= 99:
#     print("Woda jest w stanie cieklym")
# else:
#     print("Woda jest w stanie gazowym")

# 11. 5 liczb i największa z nich
# Pobierz 5 liczb od użytkownika i wypisz największą z nich.

# max_num = 0

# for i in range(1,6):
#     num = int(input(f"Podaj liczbe nr {i}: "))
#     if num > max_num:
#         max_num = num

# print(f"Najwieksza liczba jest: {max_num}")


# 12. Suma liczb parzystych od 1 do N
# Pobierz liczbę N i oblicz sumę wszystkich liczb parzystych od 1 do N.

# n = int(input("Podaj liczbe N: "))
# sum_even = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum_even = sum_even + i
        
# print(f"Suma liczb parzystych w przedziale od 1 do {n} to: {sum_even}")


# 13. Zgadnij liczbę
# Wylosuj liczbę od 1 do 20. Poproś użytkownika o zgadywanie aż do trafienia. Po każdej próbie podpowiedz, czy liczba jest większa czy mniejsza.

import random
random_number = random.randint(1, 20)

print("Zgadnij liczbe z przedzialu 1 - 20")

while True:
    user_guess = int(input("Podaj liczbe: "))
    
    if random_number == user_guess:
        print(f"Zgadles! Ta liczba to: {random_number}")
        break
    elif user_guess < random_number:
        print(f"Liczba jest wieksza od {user_guess}")
    else:
        print(f"Liczba jest mniejsza od {user_guess}")


# 14. Tabliczka mnożenia dla wybranej liczby
# Pobierz liczbę i wypisz jej tabliczkę mnożenia od 1 do 10.



# 15. Sprawdzanie liczb pierwszych
# Pobierz liczbę i sprawdź, czy jest liczbą pierwszą (czyli dzieli się tylko przez 1 i samą siebie).

