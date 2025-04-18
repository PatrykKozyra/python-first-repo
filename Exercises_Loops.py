#  1. 
# nums = [12,7,4,3,2,8,9]
# Napisz pętlę, która w princie dźwiga liczbę do potęgi drugiej, jeśli jest parzysta

nums = [12,7,4,3,2,8,9]

for num in nums:
    if num % 2 == 0:
        print(f"Liczba {num} do potegi drugiej to:")
        print(num * num)


# 2.
# Fizz Buzz to gra, która polega na tym, że gracze na zmianę wypowiadają liczby, 
# ale jeśli liczba jest podzielna przez 3, mówią "Fizz", 
# z kolei jeśli jest podzielna przez 5, mówią "Buzz". 
# Jeśli liczba jest podzielna zarówno przez 3, jak i 5, mówią "FizzBuzz"

# Za pomocą pętli i instrukcji warunkowych, spróbuj napisać algorytm FizzBuzz
# w którym gracze liczą do liczby 101


for i in range(1,101):
    print(f"Liczba to: {i}")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")


# 3. Napisz program, który obliczy sumę wszystkich liczb parzystych od 1 do podanej liczby n (włącznie).
# - w inpucie podajemy liczbę, konwertujemy - potem pętla np. range

num = int(input("Podaj liczbe: "))
sum = 0

for i in range(1, num):
    if i % 2 == 0:
        sum = sum + i
        
print(f"Suma to: {sum}")


# 4. Poproś użytkownika o wpisanie słowa i wypisz je za pomocą petli w odwrotnej kolejności, znak po znaku (nie używaj [::-1]) 

word = input("Podaj slowo: ")

for i in word[::-1]:
    print(i)