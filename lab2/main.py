#Zadanie 1
# list = ['Piłka nożna', 'koszykowka', 'boks']
# list.reverse()
# list.append('siatkówka')
# list.append('boks')
# print(list)
#Zadanie 2
# slownik = {1:"TeleGazeta" ,2:"W sieci" ,3:"Magazyn" ,4.5:"Gazeta wyborcza", "cos":"Fakt",4.6:'wartosci'}
# print(slownik)

#Zadanie 3
# Gry = {'gry1':"FIFA 22" ,'gry2':"Dying Light 2" ,'gry3':"Cyberpunk" ,'gry4':"Spiderman" ,'gry5':"CS GO" ,'gry6':"LOL"}
# print(Gry.values())

#Zadanie 4
#Napisz skrypt, który pobiera od użytkownika zdanie i liczby wystąpienia litery a. Użyj funkcji input
# napis = input('Zdanie:')
# print(napis)
# litera = 0
# for char in napis:
#     if char == 'a':
#         litera+=1
# print(litera)

#Zadanie 5
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite,gdzie wykonasz obliczenia:a^b+c. Użyj instrukcji readline() i write()).
# import sys as system
# a = (system.stdin.readline())
# b = (system.stdin.readline())
# c = (system.stdin.readline())
# wynik = a**b+c
# system.stdout.write(str(wynik))

#Zadanie 6
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if a > b:
#     if a > c:
#         maks = a
#         print('najwieksza: ',(maks))
#     else:
#         maks = c
# elif b > a:
#     if b > c:
#         maks = b
#         print('najwieksza: ',(maks))
#     else:
#         maks = c
#         print('najwieksza: ',(maks))

#Zadanie 7
# lista1 = [3, 6.0, 2, 8.0]
# lista2 = []
# print(lista1)
# for i in range(len(lista1)):
#     lista2.append(lista1[i]**2)
# print(lista2)

#Zadanie 8
# lista = []
# for i in range(1, 11):
#     print(i)
# ile = 0
# while ile < 10:
#     ile += 1
#     if i % 2 == 0:
#         lista.append(i)
# print(lista)

#Zadanie 9
# import math
# liczba = int(input("Podaj liczbę: "))
# try:
#     print(math.sqrt(liczba))
# except ValueError:
#     print("Podałeś ujemna liczba")
