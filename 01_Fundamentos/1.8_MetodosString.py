palavra = ' Desenvolvedor Python SENIOR '

print(f'Texto em Maiuscuolo: {palavra.upper()}')
print(f'Texto em Minusculo: {palavra.lower()}')
print(f'Tamanho da Palavra com espaços: {len(palavra)}')
print(f'Tamanho da Palavra sem espaços: {len(palavra.strip())}')
print(f'Substituindo Parte do Texto {palavra.replace("SENIOR", "Master")}')