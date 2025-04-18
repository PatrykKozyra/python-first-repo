# 1. 
# Napisz 3 zmienne zawierające imię, nazwisko i miasto użytkownika.
# Następnie napisz zmienną wynik w której za pomocą konkatenacji połączysz powyższe zmienne i inne słowa w zdanie:
# "To jest Jan Kowalski. Jego miejsce urodzenia to Poznań"


imie = "Jan"
nazwisko = "Kowalski"
miasto = "Poznan"

result1 = f"To jest {imie} {nazwisko}. Jego miejsce urodzenia to {miasto}"
print("EX.1:")
print(result1)
print("")

# 2.
# W twoim programie znajduje się zmienna:
# result = "to jest krótkie zdanie na temat Jana"
# Za pomocą odpowiedniej metody zastąp wszystkie spacje " ", myślnikami "-". Wynik zapisz w nowej zmiennej i wyświetl ją w konsoli

result2 = "to jest krotkie zdanie na temat Jana"
result2 = result2.replace(" ", "-")
print("EX.2:")
print(result2)
print("")

# 3.
# W twoim programie znajduje się zmienna:
# greeting = "hello world"

greeting = "hello world"

# a) W nowej zmiennej za pomocą odpowiedniej metody policz długość stringa z powyższej zmiennej
result3a = len(greeting)
print("EX.3a:")
print(result3a)
print("")
# b) W kolejnej zmiennej dźwignij wszystkie litery zmiennej do dużej litery
result3b = greeting.upper()
print("EX.3b:")
print(result3b)
print("")
# c) W jeszcze jednej zmiennej dźwignij do dużej litery tylko pierwszą literę
result3c = greeting.capitalize()
print("EX.3c:")
print(result3c)
print("")


# 4.
# W twoim programie znajduje się zmienna:
# movie = "lord of the rings"
# Za pomocą odpowiedniej metody dźwignij pierwszą literę każdego wyrazu do dużej litery

movie1 = "lord of the rings"
result4 = movie1.title()
print("EX.4:")
print(result4)
print("")

# 5.
# W twoim programie znajduje się zmienna:
# movie = "dzisiaj jest sobota"

# Za pomocą odpowiedniej metody sprawdź jaka litera znajduję się na 5 miejscu w stringu

movie2 = "dzisiaj jest sobota"
result5 = movie2[4]
print("EX.5:")
print(result5)
print("")

#Napisz funkcjonalnosc, ktora pozwoli odwrocic stringa (zapisac slowo od konca)
movie3 = "dzisiaj jest sobota"
reversed_movie3 = movie3[::-1]
print("EX.6:")
print("Original string: " + movie3)
print("Reversed string: " + reversed_movie3)
print("")


#Napisz funkcje ktora zlicza ilosc wystapien znaku
movie4 = "dzisiaj jest sobota"
count_j = movie4.count("j")
print("EX.7:")
print("String: " + movie4)
print("Count of j: " + str(count_j))