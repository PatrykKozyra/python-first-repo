firstname = "Anna"
city = "Warszawa"
street = 'Krakowska'


result = f"To jest {firstname}. Jej miejsce urodzenia to {city}."


result2 = "To jest %s. Jej miejsce zamieszkania to %s" % (firstname, city)
result3 = "To jest {}. Jej miejsce urodzenia to {}".format(firstname, city)

print(result)
print(result2)
print(result3)

###################################################################

upper = "test".upper()
print("Upper: " + upper)

capitalize = "test".capitalize()
print("Capitalize: " + capitalize)

casefold = "test".casefold()
print("Casefold: " + casefold)

# center = "test".center()
# print("Center: " + center)



text = 'geeKs For geEkS'
print("\nConverted String:")
print(text.upper())