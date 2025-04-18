# 1. Zadanie: Oblicz sumę wszystkich elementów na liście
# Dane: [1, 2, 3, 4, 5]
# el = [1, 2, 3, 4, 5]

# from functools import reduce
# sum_el = reduce(lambda x, y: x + y, el,0)
# print(sum_el)


# 2. Zadanie: Znajdź największy element w liście
# Dane: [15, 3, 10, 4, 22]
# el = [15, 3, 10, 4, 22]
# sorted_el = sorted(el, key=lambda x: x)
# print(sorted_el[-1])

# 3. Zadanie: Usuń wszystkie wystąpienia określonej liczby z listy
# Dane: [2, 5, 3, 5, 7, 5] Usuwana liczba: 5
# el = [2, 5, 3, 5, 7, 5]
# to_be_removed = 5
# modified_el = list(filter(lambda x: x != 5, el))
# print(modified_el)


# 4. Zadanie: Zwróć nową listę, w której wszystkie elementy są pomnożone przez 2
# Dane: [1, 2, 3, 4, 5]
# el = [1, 2, 3, 4, 5]
# modified_el = list(map(lambda x: x * 2, el))
# print(modified_el)


# 5. Zadanie: Sprawdź, czy lista zawiera określoną liczbę
# Dane: [3, 7, 12, 9, 20] Szukana liczba: 9
# el = [3, 7, 12, 9, 20] 
# wanted_digit = 9

# if wanted_digit in el:
#     print(f"Number {wanted_digit} exsists in the list.")
# else:
#     print(f"Number {wanted_digit} does not exsists in the list.")

# 6. Zadanie: Zwróć listę posortowaną rosnąco
# Dane: [5, 2, 9, 1, 6, 7]
# el = [5, 2, 9, 1, 6, 7]
# sorted_el_asc = sorted(el, key=lambda x: x)
# print(sorted_el_asc)

# 7. Zadanie: Zwróć listę posortowaną malejąco
# Dane: [1, 3, 8, 4, 7]
# el = [1, 3, 8, 4, 7]


# 8. Zadanie: Zwróć tylko unikalne elementy z listy (usuń duplikaty)
# Dane: [1, 2, 3, 2, 4, 1, 5]
# el = [1, 2, 3, 2, 4, 1, 5]
# sorted_el_desc = sorted(el, reverse=True)
# print(sorted_el_desc)


# 9. Zadanie: Zwróć liczbę wystąpień określonego elementu w liście
# Dane: [10, 20, 20, 30, 20, 40] Szukana liczba: 20

# el = [10, 20, 20, 30, 20, 40]
# wanted_number = 20
# from functools import reduce

# saerch_wanted = reduce(lambda x, y: x + (1 if y == wanted_number else 0), el, 0)
# print(f"Liczba {wanted_number} wystepuje: {saerch_wanted} razy.")


# 10. Zadanie: Zwróć wszystkie liczby większe niż 10
# Dane: [5, 15, 10, 25, 8, 12]

# el = [5, 15, 10, 25, 8, 12, 40]
# modified_el = list(filter(lambda x: x > 20, el))
# print(modified_el)

# 11. Zadanie: Zwróć elementy na parzystych indeksach
# Dane: [10, 20, 30, 40, 50, 60]



# 12. Zadanie: Oblicz średnią z elementów listy
# Dane: [3, 5, 7, 9, 2]



# 13. Zadanie: Odwróć kolejność elementów w liście
# Dane: [1, 2, 3, 4, 5]



# 14. Zadanie: Zwiększ każdy element w liście o 3
# Dane: [1, 2, 3, 4, 5]



# 15. Zadanie: Wstaw element w określoną pozycję w liście
# Dane: [1, 2, 3, 4, 5] Pozycja: 2 Element do wstawienia: 99
# 16. Zadanie: Usuń element na określonym indeksie
# Dane: [10, 20, 30, 40, 50] Indeks do usunięcia: 3
# 17. Zadanie: Zwróć listę tylko z liczbami parzystymi
# Dane: [1, 2, 3, 4, 5, 6]
# 18. Zadanie: Połącz dwie listy w jedną
# Dane: [1, 2, 3] oraz [4, 5, 6]
# 19. Zadanie: Zrób z listy słownik, gdzie klucze to elementy, a wartości to ich liczba wystąpień
# Dane: [1, 2, 2, 3, 3, 3, 4]
# 20. Zadanie: Zrób nową listę, zawierającą tylko te liczby, które są większe od średniej
# Dane: [5, 12, 7, 9, 3, 8]

# Zadanie: Zgrupuj elementy w słownik, gdzie klucze to pierwsze litery słów
# Dane: ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
# Opis: Utwórz słownik, gdzie klucze