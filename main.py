from math import *

#zestaw A
#zad1
# def zad1(slownik_arg):
#     lista = []
#     for key in slownik_arg.keys():
#         if type(slownik_arg[key]) == int:
#             lista.append(key)
#     return lista
#
#
# slownik = {1: 2, "a": 3, 4.5: 1, 2: "a"}
# print(zad1(slownik))
#
# #zad2
# plik = open('tekst.txt', 'r', encoding='utf-8')
# plik.seek(24)
# znaki = plik.read(20)
# plik.close()
# duze_znaki = 0
# for znak in znaki:
#     if znak.isupper():
#         duze_znaki += 1
# if duze_znaki > 0:
#     print('Ilość dużych liter: ' + str(duze_znaki))
# else:
#     print('brak dużych liter')
#
# #zad3
# lista_a = [2, 3, 5, 1, 6, 8, 3, 6, 8, 1, 9, 2]
# lista_b = [lista_a[i] for i in range(0, len(lista_a), 2)]
# print(lista_a)
# print(lista_b)
#
# #zad4
# a = pow(pi, 3) + pow(log(64, 2) + sin(45), 1/4)
# print(round(a, 2))
#
# #zad5
# try:
#     a = int(input('Wczytaj liczbę a: '))
#     b = int(input('Wczytaj liczbę b: '))
#     wynik = a**b
#     plik = open('zadanie5.txt', 'w')
#     plik.write(str(wynik))
#     plik.close()
# except ValueError:
#     print('nie wczytano liczby całkowitej')


#zestawB
#zad1
# plik = open('tekst.txt', 'r', encoding='utf-8')
# plik.seek(63)
# znaki = plik.read(42)
# plik.close()
# male_znaki = 0
# for znak in znaki:
#     if znak.islower():
#         male_znaki += 1
# if male_znaki > 0:
#     print('Ilość małych liter: ' + str(male_znaki))
# else:
#     print('brak małych liter')
#
# #zad2
# def zad2(lista_arg):
#     lista_wynikowa = []
#     for element in lista_arg:
#         if (type(element) == int) | (type(element) == float):
#             lista_wynikowa.append(element)
#
#     return lista_wynikowa, max(lista_wynikowa), min(lista_wynikowa)
#
#
# lista = [2, 3.5, 24, 'abc', 'a', -1]
# print(zad2(lista))

#zad3
# try:
#     a = int(input('Podaj liczbę a: '))
#     b = int(input('Podaj liczbę b: '))
#     wynik = pow(sin(a), 2) + pow(cos(b), 2)
#     plik = open('zadanie3.txt', 'w')
#     if wynik == 1:
#         plik.write('jedynka trygonometryczna zachodzi')
#     else:
#         plik.write('nie zachodzi jedynka trygonometryczna')
#     plik.close()
# except ValueError:
#     print("nie wczytano liczby całkowitej")

#zad4
# lista_a = [14, 21, 3, 16, 2, 5, 1, 10]
# lista_b = [a for a in lista_a if a > lista_a[-1]]
# print(lista_a)
# print(lista_b)
#
# #zad5
# b = exp(3) + pow(log(pow(cos(36),2) + pi), 1/5)
# print(round(b, 2))




