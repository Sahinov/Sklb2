#!/usr/bin/env python3
# -*- coding: utf-8 -*-f
# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

#movies = {[my_favorite_movies[0]],[my_favorite_movies.find(', ')]}

first_film = my_favorite_movies[0:my_favorite_movies.find(', ')]
last_film = my_favorite_movies[my_favorite_movies.rfind(', ')+2:]
#second_film_pointer = my_favorite_movies[[first_film_pointer],my_favorite_movies.find(', ')]
#print(first_film, last_film)

my_movies1 = my_favorite_movies.lstrip(first_film + ', ')

second_film = my_movies1[0:my_movies1.find(', ')]

my_movies2 = my_favorite_movies.rstrip(last_film)

pre_last_film = my_movies2[my_movies2.rfind(', ')+2:-1]

print('Это все фильмы: ', my_favorite_movies)
print('Первый фильм: ', first_film, 'Второй фильм: ',second_film, 'Пердпоследний фильм: ',pre_last_film, 'Последний фильм: ',last_film)

