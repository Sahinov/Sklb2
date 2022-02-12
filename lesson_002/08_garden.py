#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

print('В саду ', garden_set)
print('На лугу ', meadow_set)

# выведите на консоль все виды цветов
flowers = set(garden + meadow)
print(flowers)

# выведите на консоль те, которые растут и там и там

i_tam_set = garden_set & meadow_set

print(i_tam_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
v_sady_set = garden_set - meadow_set

print(v_sady_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
na_lygy_set = meadow_set - garden_set
print(na_lygy_set)


