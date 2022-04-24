carrinho = []

carrinho.append(("Produto 1", 50))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 30))

total = sum([preco[1] for preco in carrinho])
print(total)
