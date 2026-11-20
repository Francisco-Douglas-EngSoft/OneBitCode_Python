# Metodos de listas em Python

# 1. append(item): adiciona um item ao final da lista.
frutas = ["Manga", "Maça"]
frutas.append("Banana")
print("append:", frutas)

# 2. extend(iteravel): adiciona varios itens ao final da lista.
frutas.extend(["Uva", "Pera"])
print("extend:", frutas)

# 3. insert(indice, item): insere um item na posicao indicada.
frutas.insert(1, "Abacaxi")
print("insert:", frutas)

# 4. remove(item): remove a primeira ocorrencia do item.
frutas.remove("Banana")
print("remove:", frutas)

# 5. pop([indice]): remove e devolve um item; sem indice, remove o ultimo.
fruta_removida = frutas.pop(0)
print("pop:", fruta_removida, frutas)

# 6. index(item): devolve o indice da primeira ocorrencia do item.
print("index:", frutas.index("Uva"))

# 7. count(item): conta quantas vezes o item aparece.
frutas.extend(["Uva", "Uva"])
print("count:", frutas.count("Uva"))

# 8. copy(): cria uma copia superficial da lista.
copia_frutas = frutas.copy()
copia_frutas.append("Limao")
print("copy - original:", frutas)
print("copy - copia:", copia_frutas)

# 9. sort(): organiza os itens em ordem crescente.
numeros = [5, 2, 8, 1]
numeros.sort()
print("sort:", numeros)

# 10. reverse(): inverte a ordem atual dos itens.
numeros.reverse()
print("reverse:", numeros)

# 11. clear(): remove todos os itens da lista.
copia_frutas.clear()
print("clear:", copia_frutas)