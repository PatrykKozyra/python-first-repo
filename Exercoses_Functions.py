#  1. Napisz funkcję, która przyjmuje 4 parametry i mnoży je ze sobą, ZWRÓĆ wynik
# def multiply(a,b,c,d):
#     return print(a * b * c* d)

# multiply(1,2,3,4)


# 2. Napisz funkcję, która przyjmuje dwa parametry i oblicza pole trójkąta, ZWRÓĆ wynik

# def triangle(a,b):
#     return (a * b)/2

# a = int(input("Podaj wartosc a: "))
# b = int(input("Podaj wartosc b: "))
# result = triangle(a,b)

# print(f"Pole trojkata to: {result}")

# 3. Napisz funkcję, która konwertuje stopnie Kelvina na stopnie Celsjusza, ZWRÓĆ wynik

# def kelvin_to_celsius(k):
#     return k - 273.15

# kelvin = int(input("Podaj stopnie w kelwinach: "))
# result = kelvin_to_celsius(kelvin)

# print(f"{kelvin} stopni kelwina to - {result} stopni celsjusza.")


# 4. 
# - Napisz funkcję która w princie wypisuje słowo dobranoc
# - Napisz funkcję, która w princie wypisuje słowo dzień dobry
# - Napisz funkcję, która sprawdza godzinę, jeśli godzina jest powyżej 18 WŁĄCZ FUNKCJĘ dobranoc, w innym przypadku
# funkcję dzień dobry 

# from datetime import datetime

# def night():
#     return print("dobranoc")

# def morning():
#     return print("dzien dobry")

# def check_time():
#     current_hour = datetime.now().hour
#     print(f"Jest godzina {current_hour}")
#     if current_hour > 18:
#         return night()
#     else:
#         return morning()
    
# check_time()

#  5.
# Napisz funkcję analyze_text, która analizuje dany tekst i zwraca słownik z informacjami:
# liczba wszystkich słów,
# liczba unikalnych słów,
# najczęściej występujące słowo (jeśli kilka – zwróć dowolne),
# długość najdłuższego słowa. 

# from collections import Counter

# def analyze_text(text):
#     words = text.replace(",", "").split()
#     total_words = len(words)
#     unique_words = len(set(words))
#     word_counts = Counter(words)
#     most_common = word_counts.most_common(1)[0][0]
#     longest_word_lenght = len(most_common)
#     print(total_words, unique_words, word_counts, most_common, longest_word_lenght)
    
# content = "To jest moj tekst, moj tekst nie moze zawierac duplikatow"

# analyze_text(content)


# from collections import Counter

# def analyze_text(text):
#     words = text.replace(",","").split()
#     total_words = len(words)
#     unique_words = len(set(words))
#     word_counts = Counter(words)
#     most_common = word_counts.most_common(1)[0][0]
#     longest_word_length = len(most_common)
#     return {
#         "total_words":total_words,
#         "unique_words": unique_words,
#         "most_common":most_common,
#         "longest_word_length": longest_word_length
#     }

# content = "To mój jest mój tekst, mój tekst nie może zawierać duplikatów"
# res = analyze_text(content)
# print(res)

# def fn(**kwargs):
#     print(kwargs)
    
# fn2(name="Jan", age = 23)
# fn2(city = "Krakow")

# fn()


#####UZYJ LAMBDA#####

#  1. Napisz funkcję, która przyjmuje 4 parametry i mnoży je ze sobą, ZWRÓĆ wynik
# multiply = lambda a,b,c,d: a*b*c*d
# result = multiply(1,2,3,4)

# print(result)


# 2. Napisz funkcję, która przyjmuje dwa parametry i oblicza pole trójkąta, ZWRÓĆ wynik

# tr_ar = lambda a,h: a*h*0.5
# area = tr_ar(int(input("Podaj podstawę trójkąta:")),int(input("Podaj wysokośc trójkąta:")))
# print(f"Pole trójkąta wynosi  {area} jednostek kwadratowych")

# 3. Napisz funkcję, która konwertuje stopnie Kelvina na stopnie Celsjusza, ZWRÓĆ wynik

# kelwin = lambda a: a-273.15
# normal_units = kelwin(int(input("Podaj temperaturę w stopniach Kelwina:")))
# print(f"Temperatura w normalnych jednostkach to {normal_units} stopni Celcjusza")


def my_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

text = "Ala ma kota 123!"
print(my_upper(text)) 