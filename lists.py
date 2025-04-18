cities = ["Warszawa", "Krakow", "Elk"]
new_cities = ["Londyn", "Berlin", "Houston"]
# first = cities[0]
# print(first)

# for city in cities:
#     print(city)

# last = cities[-1]
# last2 = cities[len(cities)-1]
# print(last)
# print(last2)

# cities.append("Szczecin")
# cities.extend(new_cities)

# cities.insert(1, "Katowice")

# cities.remove("Elk")
# cities.sort()
# cities.sort(reverse=True)

#zwraca element ktory usuwa
# cities.pop(0)

# cities.reverse()

# print(cities)


# nums = [1,2,3,4,5,7]
# new_list = []

# for num in nums:
#     res = num * num
#     new_list.append(res)
    
# print(nums)
# print(new_list)

# multiply_nums = map(lambda x: x * x, nums)
# print(list(multiply_nums))

#1wszy sposob
# users = ["Kasia", "Jan", "John"]

# map_users = list(map(lambda x: f"To jest {x}", users))
# print(map_users)


# #2gi sposob
# def change_user(x):
#     return f"To jest {x}"

# users2 = list(map(change_user, users))
# print(users2)

###################

# users = ["Kasia", "Jan", "John", "Kazimierz", "Wladyslaw"]
# nums = [1,2,3,4,5,7]
# short_names = []

#1wszy sposob
# for user in users:
#     if len(user) > 5:
#         continue
#     else:
#         short_names.append(user)
        
# print(short_names)

#2gi sposob
# short_names = list(filter(lambda x: len(x) < 5, users))
# filtered_nums = list(filter(lambda x: x%2 == 0, nums))
# print(users)
# print(short_names)

# print(nums)
# print(filtered_nums)

users = [
    {"imie": "Anna", "miasto": "Warszawa", "wiek": 38},
    {"imie": "Kamil", "miasto": "Krakow", "wiek": 31},
    {"imie": "Ola", "miasto": "Gdańsk", "wiek": 22},
    {"imie": "Michał", "miasto": "Krakow", "wiek": 31},
    {"imie": "Zuzanna", "miasto": "Poznań", "wiek": 26}
]

# user_kamil = users[1]["imie"]
# city_krakow = users[3]["miasto"]
# print(user_kamil)
# print(city_krakow)

# current_city = list(filter(lambda x: x["miasto"] == "Krakow", users))
# above_30 = list(filter(lambda a: a["wiek"] >= 30, users))
# cities2 = list(filter(lambda x: x["miasto"] == "Warszawa" and x["wiek"] >= 30, users))

# print(cities2)

# uppercase = list(map(lambda x: {
#     **x,
#     "miasto": x["miasto"].upper(),
# }, users))

# from datetime import datetime

# with_date = list(map(lambda x:{
#     **x,
#     "timestamp": datetime.now().strptime("%d/%m/%Y, %H:%M:%S")
# }, users))

# print(with_date)


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

