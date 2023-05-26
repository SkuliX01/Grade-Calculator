# Definicja Listy ktora bedzie przechowywac oceny :)
grades = input("Podaj Oceny  : ")
newArray = grades.split(" ")
#petla ktora zmienia kazdy wpis w tabeli na integer z stringa
for i in range(len(newArray)):
    newArray[i] = int(newArray[i])
#funkcja print ktora kalkuluje srednia ocen poprzez zsumowanie kazdej oceny z listy oraz podzielenie ich przez dlugosc listy
print("Twoja Średnia ocen" + sum(newArray) / len(newArray))