list1 = [2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 23, 12, 26, 102]
list2 = [5, 23, 7, 121, 8, 3, 23, 5, 6, 8, 3, 9, 6, 2123, 21, 3]

listasoma = [x + y for x, y in zip(list1, list2)]
print(listasoma)