
# 1. Stwórz pustą listę i dodaj do niej kilka liczb za pomocą metody append()

# my_list = []

# for i in range(1,8):
#     my_list.append(i)

# print(my_list)

# 2. Użyj odpowiedniej metody do połączenia dwóch poniższych list.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)
# print(list1)


# 3.Z poniższej listy, za pomocą odpowiedniej metody usuń pierwsze wystąpienie cyfry 2
# my_list = [1, 2, 3, 4, 2]
# Następnie z tej samej listy usuń ostatni element

# my_list = [1, 2, 3, 4, 2]
# first_remove = my_list.remove(2)
# print(first_remove)

# my_list.pop(-1)
# print(my_list)

# 4.Z poniższej listy znajdź numer indeksu liczby 40. Wynik przypisz do zmiennej
# my_list = [10, 20, 40, 30, 20]
# index_of_forty = my_list.index(40)
# print(index_of_forty)

# 5.
# Policz za pomocą odpowiedniej metody ilość wystąpień liczby 2 w poniższej liście
# my_list = [1, 2, 2, 3, 2, 4, 2]
# counter = my_list.count(2)
# print(counter)

# Zadanie 6: Rotacja tablicy
# Opis: Napisz funkcję rotate_list(lst, k), która przesuwa elementy listy o k miejsc w prawo. 
# Jeśli k jest większe niż długość listy, należy użyć przesunięcia cyklicznego (modulo długość listy).

# def rotate_list(lst, k):

#     if lst == []:
#         return []

#     # przesunięcie cykliczne
#     k = k % len(lst)

#     # rotacja
#     return lst[-k:] + lst[:-k]

# # Przykład
# my_list = [1, 2, 3, 4, 5]
# k = 3
# rotated = rotate_list(my_list, k)
# print(rotated)

##########################################################################################################

# 1. Użyj filter, aby wybrać loty, których cena przekracza 500 zł.
# 2. Użyj filter, aby wybrać loty, których data odlotu to 10 kwietnia 2025. 
# 3. Użyj filter, aby sprawdzić loty na kierunku Warszawa - Berlin
# 4. Użyj filter, aby sprawdzić loty na kierunku Kraków - Londyn, na których jest powyżej 250 pasażerów
# 5. Użyj map, aby dla każdego lotu zwiększyć cenę o 20%.
# 6. Użyj filter, aby wybrać tylko loty, które są obsługiwane przez samolot modelu "Boeing 777".
# 7. Użyj map, aby z każdej podróży wyciągnąć tylko kierunek, czyli nazwę miasta docelowego.

# 8. Przedstaw całkowitą liczbę pasażerów za pomocą metody reduce
# 9. Posortuj loty po ilości pasażerów (sorted)
# 10. Przedstaw łączną kwotę jaką zarobiły linie lotnicze mnożąc ceny biletów przez wszystkich pasażerów  (reduce) 

flights = [
    {'model': 'Embraer 190', 'passengers': 189, 'direction': 'Warszawa - Berlin', 'price': 300, 'departure_time': '11/04/2025, 06:50:00'},
    {'model': 'Boeing 777', 'passengers': 271, 'direction': 'Kraków - Londyn', 'price': 300, 'departure_time': '10/04/2025, 20:00:00'},
    {'model': 'Boeing 777', 'passengers': 261, 'direction': 'Poznań - Rzym', 'price': 550, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Embraer 190', 'passengers': 134, 'direction': 'Wrocław - Madryt', 'price': 700, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Embraer 190', 'passengers': 183, 'direction': 'Warszawa - Berlin', 'price': 450, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Boeing 737', 'passengers': 130, 'direction': 'Kraków - Londyn', 'price': 300, 'departure_time': '10/04/2025, 20:00:00'},
    {'model': 'Boeing 777', 'passengers': 245, 'direction': 'Kraków - Londyn', 'price': 550, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Boeing 777', 'passengers': 51, 'direction': 'Warszawa - Berlin', 'price': 700, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Embraer 190', 'passengers': 265, 'direction': 'Warszawa - Berlin', 'price': 150, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Boeing 737', 'passengers': 272, 'direction': 'Gdańsk - Paryż', 'price': 150, 'departure_time': '10/04/2025, 07:30:00'}
]

# #1
# price_above_30 = list(filter(lambda x: x["price"] > 500, flights))
# print(price_above_30)

# #2
# target_date = "10/04/2025"
# flight_10th_apr = list(filter(lambda x: x["departure_time"][:10] == target_date, flights))
# print(flight_10th_apr)

# #3
# flights_waw_ber = list(filter(lambda x: x["direction"] == "Warszawa - Berlin", flights))
# print(flights_waw_ber)

# #4
# flights_krk_lon = list(filter(lambda x: x["direction"] == "Kraków - Londyn" and x["passengers"] > 250, flights))
# print(flights_krk_lon)

# #5
# updated_flights = list(map(lambda x: {**x, 'price': x['price'] * 1.2}, flights))
# print(updated_flights)

# #6
# boeing_flights = list(filter(lambda x: x["model"] == "Boeing 777", flights))
# print(boeing_flights)

# #7
# directions = list(map(lambda x: x["direction"].split(" - ")[1],flights))
# print(directions)

#8
# from functools import reduce
# sum_passengers = reduce(lambda x, y: x + y['passengers'], flights,0)
# print(sum_passengers)

#9
# sorted_flights = sorted(flights, key=lambda x: x['passengers'])

# for x in sorted_flights:
#     print(x)
    
#10
# from functools import reduce
# revenue = reduce(lambda x, y: x + (y["passengers"] * y["price"]), flights,0)
# print(revenue)