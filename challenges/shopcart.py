carrinho = []

carrinho.append(("Produto 1", 50))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 30))

valor = [preco[1] for preco in carrinho]
total = sum(valor)
print(total)