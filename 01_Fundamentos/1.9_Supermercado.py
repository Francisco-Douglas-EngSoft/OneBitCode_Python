produto = str(input("Nome do Produto: ")).title()
valor = float(input(f'Digite o valor do {produto}: R$ '))
desconto = int(input("Digite o desconto aplicado: % "))

novo_valor = valor - (valor * (desconto / 100))
print(f'O {produto} que antes custava {valor} R$')
print(f'Com o desconto de {desconto}% seu novo valor sera de {novo_valor}R$')