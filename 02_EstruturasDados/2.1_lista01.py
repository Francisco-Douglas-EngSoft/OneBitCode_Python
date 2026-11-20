"Listas em Python"

#Lista de Produtos
produtos = []

for n in range(1, 5):
    produto = str(input(f'{n} Produto: '))
    produtos.append(produto)
print(f'Os Produtos São {produtos}')

#Pegando o Primeiro produto
print(f'Primeiro Produto {produtos[0]}')
print(f'Tamanho da Lista {len(produtos)}')