# - List comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [v for v in l1]
print(l2)

multiplicado = [v * 2 for v in l2]
print(multiplicado)

nomes = ["Caio", "Lucas", "Renato"]
lnomes = [v.replace("a", "@") for v in nomes]
print(lnomes)

numlist = list(range(100))

divbytwo = [v for v in numlist if v % 2 == 0]
print(divbytwo)

divbythreeandfive = [v for v in numlist if v % 3 == 0 if v % 5 == 0]
print(divbythreeandfive)